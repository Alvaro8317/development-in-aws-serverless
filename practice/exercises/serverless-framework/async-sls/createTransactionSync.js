'use strict';

/**
 * Simula una base de datos inestable:
 * - Latencia variable
 * - Fallas intermitentes (timeout, connection refused, throttle)
 * - Inserción que a veces "funciona" y a veces explota
 */

const randomInt = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

class DbError extends Error {
  constructor(message, code, meta = {}) {
    super(message);
    this.name = 'DbError';
    this.code = code;
    this.meta = meta;
  }
}

function pickWeighted(items) {
  const total = items.reduce((acc, x) => acc + x.weight, 0);
  let r = Math.random() * total;
  for (const it of items) {
    r -= it.weight;
    if (r <= 0) return it.value;
  }
  return items[items.length - 1].value;
}

async function connectToFakeDb() {
  await sleep(randomInt(80, 260));

  const outcome = pickWeighted([
    { value: 'OK', weight: 85 },
    { value: 'ECONNREFUSED', weight: 7 },
    { value: 'ETIMEDOUT', weight: 6 },
    { value: 'THROTTLED', weight: 2 },
  ]);

  if (outcome !== 'OK') {
    const messageByCode = {
      ECONNREFUSED: 'No se pudo abrir conexión con la BD (ECONNREFUSED)',
      ETIMEDOUT: 'Timeout conectando con la BD (ETIMEDOUT)',
      THROTTLED: 'La BD está saturada (THROTTLED)',
    };
    throw new DbError(messageByCode[outcome], outcome, {
      stage: 'connect',
      latencyMs: null,
    });
  }

  return {
    async insertTransaction(tx) {
      const queryLatency = randomInt(120, 520);
      await sleep(queryLatency);

      const insertOutcome = pickWeighted([
        { value: 'OK', weight: 80 },
        { value: 'DEADLOCK', weight: 5 },
        { value: 'WRITE_TIMEOUT', weight: 10 },
        { value: 'DISK_FULL', weight: 1 },
        { value: 'NETWORK_GLITCH', weight: 4 },
      ]);

      if (insertOutcome !== 'OK') {
        const messageByCode = {
          DEADLOCK: 'Deadlock detectado durante la inserción',
          WRITE_TIMEOUT: 'Timeout escribiendo en la BD',
          DISK_FULL: 'No hay espacio en disco (simulado)',
          NETWORK_GLITCH: 'Interrupción de red durante escritura',
        };
        throw new DbError(messageByCode[insertOutcome], insertOutcome, {
          stage: 'insert',
          latencyMs: queryLatency,
        });
      }

      return {
        insertedId: `tx_${randomInt(100000, 999999)}`,
        latencyMs: queryLatency,
      };
    },
    async close() {
      await sleep(randomInt(20, 60));
    },
  };
}

function buildFakeTransaction(event) {
  const now = new Date().toISOString();
  const merchantId = `m_${randomInt(100, 999)}`;
  const userId = `u_${randomInt(1000, 9999)}`;

  let body = {};
  try {
    body = event?.body ? JSON.parse(event.body) : {};
  } catch (_) {}

  return {
    idempotencyKey: body.idempotencyKey || `idem_${randomInt(100000, 999999)}`,
    amount: body.amount ?? amount,
    currency: body.currency || 'COP',
    merchantId: body.merchantId || merchantId,
    userId: body.userId || userId,
    createdAt: now,
    description: body.description || 'Compra en PlasticPay (simulado)',
  };
}

module.exports.createTransaction = async (event) => {
  const tx = buildFakeTransaction(event);

  console.log('Incoming transaction:', tx);

  const db = await connectToFakeDb();
  const result = await db.insertTransaction(tx);
  await db.close();

  return {
    statusCode: 201,
    body: JSON.stringify({
      message: 'Transaction stored',
      tx,
      result,
    }),
  };
};

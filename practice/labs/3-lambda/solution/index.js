let counter = 0;
let lastInvocationTime = null;
let coldStart = true;

function handleColdStart() {
  console.log("⏳ Cold start detectado. Reiniciando el contador...");
  coldStart = false;
}

function updateLastInvocationTime() {
  const now = new Date();
  lastInvocationTime = now.toLocaleString("es-CO", {
    timeZone: "America/Bogota",
  });
}

exports.handler = async (event) => {
  let message;
  counter++;
  if (coldStart) {
    handleColdStart();
    message = `❄️ Está haciendo frío, ¿no? Contador reiniciado a 0. Ahora está en: ${counter}`;
  } else {
    message = `Lambda en estado: 🔥 Última invocación: ${lastInvocationTime}`;
  }
  updateLastInvocationTime();

  console.log("✅ Estado actual del contador:", counter);

  return {
    statusCode: 200,
    body: JSON.stringify({
      message: message,
      counter: counter,
      lastInvocationTime: lastInvocationTime,
    }),
  };
};

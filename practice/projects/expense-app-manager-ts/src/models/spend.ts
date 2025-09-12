import { randomUUID } from "crypto"

export interface SpendProps {
    id: string
    name: string
    description?: string | null
    amount: number
    datetimeSpend: string
}

export class Spend implements SpendProps {
    id: string
    name: string
    description?: string | null
    amount: number
    datetimeSpend: string

    constructor(props: SpendProps) {
        this.id = props.id
        this.name = props.name
        this.description = props.description ?? null
        this.amount = props.amount
        this.datetimeSpend = props.datetimeSpend
    }

    static newSpend(name: string, amount: number, description?: string | null): Spend {
        const isoDate = new Date().toISOString().split("T")[0]
        return new Spend({
            id: randomUUID(),
            name,
            description,
            amount,
            datetimeSpend: isoDate,
        })
    }

    asDict(): Record<string, string | number | null> {
        return {
            id: this.id,
            name: this.name,
            description: this.description ?? null,
            amount: this.amount,
            datetimeSpend: this.datetimeSpend,
        }
    }

    *[Symbol.iterator](): Generator<[string, string | number | null]> {
        for (const [key, value] of Object.entries(this.asDict())) {
            yield [key, value]
        }
    }
}

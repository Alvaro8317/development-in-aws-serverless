// services/spendService.ts
import { Spend } from "../models/spend"
import { BaseRepositorySpend } from "../repositories/spendRepository"

export class SpendService {
    private repository: BaseRepositorySpend

    constructor(repository: BaseRepositorySpend) {
        this.repository = repository
    }

    /** Crea un gasto y lo guarda en el repositorio */
    async createSpend(name: string, description: string | null, amount: number): Promise<Spend> {
        const spendItem = Spend.newSpend(name, amount, description)
        await this.repository.createSpend(spendItem.asDict())
        return spendItem
    }

    /** Obtiene todos los gastos desde el repositorio */
    async getSpends(): Promise<Spend[]> {
        return this.repository.getSpends()
    }
}

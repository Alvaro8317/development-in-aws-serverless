import { handler } from "../src/spend";

describe("Spend handler", () => {
  it("should return a successful response", async () => {
    const response = await handler({
      body: JSON.stringify({
        name: "Test",
        description: "Unit test",
        amount: "123.45"
      })
    } as any);

    expect(response.statusCode).toBe(200);
    const body = JSON.parse(response.body);
    expect(body.message).toBe("Spend created successfully");
    expect(body.spend).toHaveProperty("id");
  });
});
from google.adk import Agent

hotel_agent = Agent(
    name = "hotel_agent",
    model = "gemini-2.0-flash-exp",
    description = "Finds hotels using origin, destination, travel dates and budgets",
    instruction = """
                    You are a hotel booking agent. The coordinator will give you:
                    - destination
                    - start_date
                    - end_date
                    - budget_amount
                    - budget_currency

                    Return 1-2 mock hotel options including:
                    - Hotel name
                    - Nightly price in the specified currency
                    - Main features

                    Make sure the total price is within budget.
                  """
)
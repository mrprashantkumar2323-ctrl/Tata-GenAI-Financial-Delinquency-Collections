"""
Agentic AI Collections Strategy Orchestrator (Geldium System)
Author: Prashant Kumar
"""

class AgenticCollectionsEngine:
    def __init__(self, risk_model):
        self.risk_model = risk_model

    def evaluate_account(self, customer_profile):
        """
        Agentic decision loop determining autonomous vs human-supervised collection interventions.
        """
        # Risk tiering
        prob = customer_profile.get("delinquency_probability", 0.3)
        utilization = customer_profile.get("credit_utilization", 0.5)
        dti = customer_profile.get("debt_to_income", 0.35)

        action_plan = {}
        if prob < 0.25:
            action_plan["tier"] = "Low Risk (Tier 1)"
            action_plan["channel"] = "Autonomous Smart SMS & In-App Notification"
            action_plan["message"] = "Friendly automated payment reminder with 1-click UPI pay link."
            action_plan["requires_human_approval"] = False
        elif 0.25 <= prob < 0.65:
            action_plan["tier"] = "Moderate Risk (Tier 2)"
            action_plan["channel"] = "Dynamic WhatsApp + Personalized Restructuring Offer"
            action_plan["message"] = "Offer automated EMI split or waiver on late fee for repayment within 48h."
            action_plan["requires_human_approval"] = False
        else:
            action_plan["tier"] = "High Risk / Hardship (Tier 3)"
            action_plan["channel"] = "Human Specialist Escalation"
            action_plan["message"] = "Direct transfer to customer care specialist for structured hardship relief."
            action_plan["requires_human_approval"] = True

        return action_plan

if __name__ == "__main__":
    agent = AgenticCollectionsEngine(risk_model=None)
    test_cases = [
        {"delinquency_probability": 0.12, "name": "Customer A"},
        {"delinquency_probability": 0.48, "name": "Customer B"},
        {"delinquency_probability": 0.78, "name": "Customer C"}
    ]
    print("=== Agentic AI Collections Orchestration Plan ===")
    for c in test_cases:
        plan = agent.evaluate_account(c)
        print(f"
{c['name']} -> {plan['tier']}")
        print(f"  Channel: {plan['channel']}")
        print(f"  Action:  {plan['message']}")
        print(f"  Escalation: {'Yes (Human-in-the-loop)' if plan['requires_human_approval'] else 'Autonomous'}")

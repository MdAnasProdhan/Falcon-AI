class PlannerPlugin:

    def handle(self, text):

        if text == "plan my day":

            return """Today's Plan

1. Check Amazon deliveries
2. Complete priority orders
3. Study Falcon AI
4. Exercise
5. Sleep on time"""

        elif text == "plan falcon":

            return """Falcon AI Roadmap

1. Improve Memory
2. Add Planner
3. Add Voice
4. Add Android Controller
5. Add Windows Controller"""

        elif text == "plan amazon":

            return """Amazon Delivery Plan

1. Check queue
2. Accept deliveries
3. Follow best route
4. Complete deliveries
5. Update delivery status"""

        return None


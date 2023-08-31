from pymongo.collection import Collection

class SubscriptionModel:
    def __init__(self, collection: Collection):
        self.collection = collection

    def create_subscription(self, user_id, username, start_date, end_date, remaining_payment):
        # Create a new subscription document
        # ...

    def get_subscription_by_user_id(self, user_id):
        # Retrieve subscription by user ID
        # ...

    def update_subscription(self, user_id, new_data):
        # Update subscription data
        # ...

# Other model definitions
# ...

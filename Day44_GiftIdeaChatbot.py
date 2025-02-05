import random

class GiftIdeaWizard:
    def __init__(self):
        self.gift_categories = {
            'tech': ['Smart Watch', 'Wireless Earbuds', 'Portable Charger'],
            'creative': ['Art Set', 'DIY Craft Kit', 'Digital Drawing Tablet'],
            'fitness': ['Fitness Tracker', 'Yoga Mat', 'Workout Accessories'],
            'home': ['Smart Speaker', 'Indoor Plant Kit', 'Gourmet Cooking Set']
        }
        
        self.age_recommendations = {
            'child': ['LEGO Set', 'Board Game', 'Science Experiment Kit'],
            'teen': ['Bluetooth Speaker', 'Gaming Accessories', 'Trendy Backpack'],
            'adult': ['Wireless Headphones', 'Smartwatch', 'Portable Bluetooth Speaker'],
            'senior': ['Easy-to-Use Tablet', 'Comfortable Slippers', 'Health Monitoring Device']
        }

    def start_conversation(self):
        print("🎁 Welcome to the AI Gift Idea Wizard! 🎁")
        return self.ask_recipient_age()

    def ask_recipient_age(self):
        print("\nWhat is the recipient's age group?")
        print("1. Child (0-12)")
        print("2. Teen (13-19)")
        print("3. Adult (20-59)")
        print("4. Senior (60+)")
        
        choice = input("Enter number: ")
        age_map = {
            '1': 'child', 
            '2': 'teen', 
            '3': 'adult', 
            '4': 'senior'
        }
        
        return self.ask_interests(age_map.get(choice, 'adult'))

    def ask_interests(self, age_group):
        print(f"\nWhat interests does the {age_group} have?")
        print("1. Technology")
        print("2. Creative Arts")
        print("3. Fitness")
        print("4. Home & Lifestyle")
        
        choice = input("Enter number: ")
        interest_map = {
            '1': 'tech', 
            '2': 'creative', 
            '3': 'fitness', 
            '4': 'home'
        }
        
        return self.generate_recommendations(age_group, interest_map.get(choice, 'tech'))

    def generate_recommendations(self, age_group, interest):
        age_gifts = self.age_recommendations.get(age_group, [])
        category_gifts = self.gift_categories.get(interest, [])
        
        combined_gifts = age_gifts + category_gifts
        recommendations = random.sample(combined_gifts, min(3, len(combined_gifts)))
        
        print("\n🎉 Gift Recommendations 🎉")
        for idx, gift in enumerate(recommendations, 1):
            print(f"{idx}. {gift}")
        
        return self.get_budget_preference()

    def get_budget_preference(self):
        print("\nWhat's your budget range?")
        print("1. Budget-Friendly ($20-$50)")
        print("2. Mid-Range ($50-$150)")
        print("3. Premium ($150-$500)")
        
        budget_choice = input("Enter number: ")
        budget_map = {
            '1': 'Budget-Friendly',
            '2': 'Mid-Range',
            '3': 'Premium'
        }
        
        print(f"\nThanks! We'll focus on {budget_map.get(budget_choice, 'Mid-Range')} options.")
        print("Enjoy your gift shopping! 🎁")

def main():
    wizard = GiftIdeaWizard()
    wizard.start_conversation()

if __name__ == "__main__":
    main()
    

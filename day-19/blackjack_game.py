import random

def get_user_choice(user_choice: str) -> str:
    """Get user input and ensure it's valid."""
    while True:
        choice = input(user_choice).lower()
        if choice in ["yes", "no"]:
            return choice
        print("Invalid input. Please enter 'Yes' or 'No'.")

def draw_cards(num_cards=2) -> list:
    """Draw 2 cards from a deck with values from 1-10."""
    return random.sample(range(1, 11), num_cards)

def calculate_sum(cards: list) -> int:
    """Calculate the total sum of the given cards."""
    return sum(cards)

def main():
    should_game_continue = True

    while should_game_continue:
        user_choice = get_user_choice("Do you want to play? Yes or No: ")

        if user_choice == "no":
            should_game_continue = False
            print("Thank you for playing!")
            break

        user_cards = draw_cards()
        computer_cards = draw_cards()

        print(f"Your cards: {user_cards[0]}, {user_cards[1]}")
        print(f"Computer's card: {computer_cards[0]}")

        while True:  
            should_draw_more = get_user_choice("Do you want to draw more? Yes or No: ")

            if should_draw_more == "no":
                break

            user_cards.append(random.randint(1, 10))
            user_total = calculate_sum(user_cards)

            if user_total > 21:
                print(f"Your cards: {user_cards} - Sorry, your sum is greater than 21. You lose!")
                break 
            else:
                print(f"Your cards after drawing: {user_cards}")

        if user_total <= 21: 
            print(f"Your final cards: {user_cards}")
            print(f"Computer's cards: {computer_cards}")

            user_total = calculate_sum(user_cards)
            computer_total = calculate_sum(computer_cards)

            if user_total > computer_total:
                print("Congratulations! You are the winner!")
            elif user_total < computer_total:
                print("We're sorry, you did not win :(")
            else:
                print("It's a DRAW!")

if __name__ == "__main__":
    main()

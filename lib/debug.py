

from models import Restaurant, Review, Customer, session

#Get the first customer and print their reviewed restaurants
first_customer = session.query(Customer).first()
print(f"Restaurants reviewed by {first_customer.full_name()}:")
for restaurant in first_customer.customer_restaurants():
    print(restaurant)

# Get the first review and print its details
first_review = session.query(Review).first()
print(f"Details of the first review:")
print(f"Rating: {first_review.star_rating}")
print(f"Restaurant: {first_review.review_restaurant().name}")
print(f"Customer: {first_review.review_customer().full_name()}")

#  Get the fanciest restaurant and print its details
fanciest_restaurant = Restaurant.restaurant_fanciest()
print(f"The fanciest restaurant is: {fanciest_restaurant.name}")
print(f"Price: {fanciest_restaurant.price}")

# Get all reviews for the fanciest restaurant and print them
print(f"Reviews for {fanciest_restaurant.name}:")
for review in fanciest_restaurant.restaurant_all_reviews():
    print(review)

# Add a review for the fanciest restaurant by the first customer
fanciest_restaurant_id = fanciest_restaurant.id
rating = 9
first_customer.customer_add_review(fanciest_restaurant, rating)
session.commit()

# Print all reviews for the fanciest restaurant again
print(f"Reviews for {fanciest_restaurant.name} after adding a new review:")
for review in fanciest_restaurant.restaurant_all_reviews():
    print(review)

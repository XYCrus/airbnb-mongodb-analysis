# AirBnB MongoDB Analysis

## Preview

This repository involves importing and analyzing data within a MongoDB database.

The goals are to:

- import the text data file into MongoDB document-oriented database collection
- perform queries in MongoDB to gain insights present in the data

## Data Set Details

I will use the dataset of [AirBnB in Hawaii](http://data.insideairbnb.com/united-states/hi/hawaii/2021-12-11/data/listings.csv.gz) from the official AirBnb database website.

The original data is in CSV format and the first few rows look like the following:


| id   | listing_url                       | scrape_id      | last_scraped | name                                      | description                         | neighborhood_overview          | picture_url                                                                                                 | host_id      | ... |
| :--- | :---------------------------------| :------------- | :----------- | :---------------------------------------- | :---------------------------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------- | :----------- | :-- |
| 5269 | https://www.airbnb.com/rooms/5269 | 20211211051353 | 2021-12-12   | Upcountry Hospitality in the 'Auwai Suite | "The 'Auwai Suite is a lovely...    | We are located on...           | https://a0.muscache.com/pictures/5b52b72f-5a09-4218-a0c8-ec581f872a35.jpg                                   | Lea & Pat    | ... |
| 5387 | https://www.airbnb.com/rooms/5387 | 20211211051353 | 2021-12-12   | Hale Koa Studio & 1 Bedroom Units!!       | "This Wonderful Spacious Studio...  | This duplex has a wonderful... | https://a0.muscache.com/pictures/1170713/dca6af5f_original.jpg                                              | Captain Cook | ... |
| 5389 | https://www.airbnb.com/rooms/5389 | 20211211051353 | 2021-12-12   | Keauhou Villa                             | "It is less than 10 minute...       | We take our Airbnb hosting...  | https://a0.muscache.com/im/pictures/user/b895b9d9-e59c-42c9-980c-63808ac90324.jpg?aki_policy=profile_small  | Kailua Kona  | ... |
| ...  | ...                               | ...            | ...          | ...                                       | ...                                 | ...                            | ...                                                                                                         | ...          | ... |

In order to perform analysis based on host and review_score, I performed row_wise removal of null value in these columns.

## Analysis
* In this section, I will only show the first two documents in the result and add a few notes regarding the result

1. Exactly two documents from the `listings` collection in any order

Nothing worth mentioning...

```
db.listings.find().limit(2)
```
```
{ "_id" : ObjectId("6245ed7421f2b8ef609bca69"), "" : 9, "id" : 13527, "listing_url" : "https://www.airbnb.com/rooms/13527", "scrape_id" : NumberLong("20211211051353"), "last_scraped" : "2021-12-11", "name" : "Romantic Ocean Front", "description" : "Please note this unit has a seven day minimum stay due to the complex rules.  It is a a true ocean front unit with a small private beach, park like grounds, ocean front bbq, heated pool, reserved parking and a truly charming tropical chic decor.<br /><br /><b>The space</b><br />Ocean Front, heated pool, private beach, parklike grounds, reserved parking, wifi, fully stocked unit, ocean front Dining/BBQ area<br /><br /><b>Guest access</b><br />there is a small library/office on the property so if you forgot a good read please help yourself to the library adjacent to the front office.  Also be sure and check out the salt water pool over the wall which is public access.  When the waves crash into the pool it is a treat to swim in the pool.<br /><br /><b>Other things to note</b><br />Like the majority of the units on the grounds we no longer feel the need for a/c.  We have plans to remodel and remove the wall where the a/c unit sits but please note it is not operational. We no longer supply", "neighborhood_overview" : "Kona Isle is conveniently located about a twenty minute walk to town where you will enjoy local fruits, vegetables, flowers, and gifts at the market on your way to Kona town.", "picture_url" : "https://a0.muscache.com/pictures/63448/2f168bfb_original.jpg", "host_id" : 52967, "host_url" : "https://www.airbnb.com/users/show/52967", "host_name" : "Beth", "host_since" : "2009-11-10", "host_location" : "Santa Rosa, California, United States", "host_about" : "", "host_response_time" : "within a few hours", "host_response_rate" : "100%", "host_acceptance_rate" : "", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/users/52967/profile_pic/1344745611/original.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/users/52967/profile_pic/1344745611/original.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Kailua/Kona", "host_listings_count" : 2, "host_total_listings_count" : 2, "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'kba']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "Kailua-Kona, Hawaii, United States", "neighbourhood_cleansed" : "North Kona", "neighbourhood_group_cleansed" : "Hawaii", "latitude" : 19.61632, "longitude" : -155.98305, "property_type" : "Entire place", "room_type" : "Entire home/apt", "accommodates" : 4, "bathrooms" : "", "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : "", "amenities" : "[\"Bed linens\", \"TV with standard cable\", \"Washer\", \"Kitchen\", \"Wifi\", \"Hot water\", \"Hangers\", \"Dishes and silverware\", \"Pool\", \"Essentials\", \"Dedicated workspace\", \"Free parking on premises\", \"Coffee maker\", \"Iron\", \"Stove\", \"Cooking basics\", \"Oven\", \"Refrigerator\", \"Dryer\", \"Long term stays allowed\", \"Cable TV\"]", "price" : "$169.00", "minimum_nights" : 30, "maximum_nights" : 120, "minimum_minimum_nights" : 30, "maximum_minimum_nights" : 30, "minimum_maximum_nights" : 120, "maximum_maximum_nights" : 120, "minimum_nights_avg_ntm" : 30, "maximum_nights_avg_ntm" : 120, "calendar_updated" : "", "has_availability" : "t", "availability_30" : 0, "availability_60" : 22, "availability_90" : 30, "availability_365" : 120, "calendar_last_scraped" : "2021-12-11", "number_of_reviews" : 7, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "2017-01-02", "last_review" : "2020-01-06", "review_scores_rating" : 3.83, "review_scores_accuracy" : 3.67, "review_scores_cleanliness" : 3.17, "review_scores_checkin" : 4.33, "review_scores_communication" : 4, "review_scores_location" : 4.83, "review_scores_value" : 3.83, "license" : "", "instant_bookable" : "f", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 1, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.12 }
{ "_id" : ObjectId("6245ed7421f2b8ef609bca60"), "" : 0, "id" : 5269, "listing_url" : "https://www.airbnb.com/rooms/5269", "scrape_id" : NumberLong("20211211051353"), "last_scraped" : "2021-12-12", "name" : "Upcountry Hospitality in the 'Auwai Suite", "description" : "The 'Auwai Suite is a lovely, self-contained apartment at the back of our historic Waimea Guest House built in the 1800's. This suite is named for the 100-year-old Hawaiian irrigation canal that runs through the property. <br /><br />It has a full kitchen, dining area, beautifully tiled bathroom, bedroom with queen bed and two window seats, a shared back lanai, and a private outdoor table and chairs. <br />This is a most popular suite in Waimea Guest House and is great for extended stays.<br /><br /><b>The space</b><br />The ‘Auwai Suite is a lovely, self-contained apartment at the back of Waimea Guest House. It has a full kitchen, dining area, and beautifully tiled bathroom, as well as a large bedroom - with high vaulted ceilings, a queen bed, and two window seats - that opens out onto a shared back lanai. <br /><br />To find the entrance to this unit, guests follow the traditional Hawaiian ‘auwai (irrigation ditch) that runs along the property towards the back. The most private of th", "neighborhood_overview" : "We are located on the \"sunny side\" of Waimea, just off the Kawaihae Road.  Our home is tucked into a quiet residential neighborhood at the base of the Kohala mountain range.", "picture_url" : "https://a0.muscache.com/pictures/5b52b72f-5a09-4218-a0c8-ec581f872a35.jpg", "host_id" : 7620, "host_url" : "https://www.airbnb.com/users/show/7620", "host_name" : "Lea & Pat", "host_since" : "2009-02-09", "host_location" : "Waimea, Hawaii, United States", "host_about" : "Lea, born and raised on the Island of Hawaii, just returned with her husband, Pat. We think Waimea is the very best place to live -- central, a little cooler and surrounded by an adorable town.  We offer Hawaiian hospitality to travelers who are looking for an authentic island experience.  We love the Big Island and know it well. The best part of hosting is getting to share tips and tricks with our guests and make sure they see the real deal while staying with us.  ", "host_response_time" : "within a few hours", "host_response_rate" : "86%", "host_acceptance_rate" : "46%", "host_is_superhost" : "t", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/16ac6af1-4484-45ec-929b-5fcae8fdce66.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/16ac6af1-4484-45ec-929b-5fcae8fdce66.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Island of Hawaiʻi", "host_listings_count" : 2, "host_total_listings_count" : 2, "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'offline_government_id', 'kba', 'selfie', 'government_id', 'identity_manual']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "Kamuela, Hawaii, United States", "neighbourhood_cleansed" : "South Kohala", "neighbourhood_group_cleansed" : "Hawaii", "latitude" : 20.0274, "longitude" : -155.702, "property_type" : "Entire rental unit", "room_type" : "Entire home/apt", "accommodates" : 2, "bathrooms" : "", "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Bed linens\", \"Shared hot tub\", \"TV with standard cable\", \"Kitchen\", \"Fire extinguisher\", \"Wifi\", \"Hot water\", \"Hangers\", \"Pack \\u2019n play/Travel crib\", \"Dishes and silverware\", \"BBQ grill\", \"Free street parking\", \"Children\\u2019s books and toys\", \"Essentials\", \"Breakfast\", \"Patio or balcony\", \"Backyard\", \"Beach essentials\", \"Dedicated workspace\", \"Smoke alarm\", \"Baking sheet\", \"Luggage dropoff allowed\", \"Shower gel\", \"Coffee maker\", \"Iron\", \"Hair dryer\", \"Babysitter recommendations\", \"Stove\", \"Cooking basics\", \"Oven\", \"Refrigerator\", \"Extra pillows and blankets\", \"Outdoor furniture\", \"Long term stays allowed\", \"Cable TV\"]", "price" : "$149.00", "minimum_nights" : 3, "maximum_nights" : 200, "minimum_minimum_nights" : 3, "maximum_minimum_nights" : 5, "minimum_maximum_nights" : 200, "maximum_maximum_nights" : 200, "minimum_nights_avg_ntm" : 3.8, "maximum_nights_avg_ntm" : 200, "calendar_updated" : "", "has_availability" : "t", "availability_30" : 0, "availability_60" : 0, "availability_90" : 0, "availability_365" : 193, "calendar_last_scraped" : "2021-12-12", "number_of_reviews" : 16, "number_of_reviews_ltm" : 6, "number_of_reviews_l30d" : 0, "first_review" : "2011-05-31", "last_review" : "2021-10-23", "review_scores_rating" : 4.53, "review_scores_accuracy" : 4.87, "review_scores_cleanliness" : 4.27, "review_scores_checkin" : 5, "review_scores_communication" : 4.87, "review_scores_location" : 5, "review_scores_value" : 4.8, "license" : "119-269-5808-01R", "instant_bookable" : "f", "calculated_host_listings_count" : 2, "calculated_host_listings_count_entire_homes" : 2, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.12 }
```

2. Exactly 10 documents in any order using the `pretty()` function.

Well it is prettier...

```
db.listings.find().limit(10).pretty()
```
```
{
	"_id" : ObjectId("6245ed7421f2b8ef609bca69"),
	"" : 9,
	"id" : 13527,
	"listing_url" : "https://www.airbnb.com/rooms/13527",
	"scrape_id" : NumberLong("20211211051353"),
	"last_scraped" : "2021-12-11",
	"name" : "Romantic Ocean Front",
	"description" : "Please note this unit has a seven day minimum stay due to the complex rules.  It is a a true ocean front unit with a small private beach, park like grounds, ocean front bbq, heated pool, reserved parking and a truly charming tropical chic decor.<br /><br /><b>The space</b><br />Ocean Front, heated pool, private beach, parklike grounds, reserved parking, wifi, fully stocked unit, ocean front Dining/BBQ area<br /><br /><b>Guest access</b><br />there is a small library/office on the property so if you forgot a good read please help yourself to the library adjacent to the front office.  Also be sure and check out the salt water pool over the wall which is public access.  When the waves crash into the pool it is a treat to swim in the pool.<br /><br /><b>Other things to note</b><br />Like the majority of the units on the grounds we no longer feel the need for a/c.  We have plans to remodel and remove the wall where the a/c unit sits but please note it is not operational. We no longer supply",
	"neighborhood_overview" : "Kona Isle is conveniently located about a twenty minute walk to town where you will enjoy local fruits, vegetables, flowers, and gifts at the market on your way to Kona town.",
	"picture_url" : "https://a0.muscache.com/pictures/63448/2f168bfb_original.jpg",
	"host_id" : 52967,
	"host_url" : "https://www.airbnb.com/users/show/52967",
	"host_name" : "Beth",
	"host_since" : "2009-11-10",
	"host_location" : "Santa Rosa, California, United States",
	"host_about" : "",
	"host_response_time" : "within a few hours",
	"host_response_rate" : "100%",
	"host_acceptance_rate" : "",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/users/52967/profile_pic/1344745611/original.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/users/52967/profile_pic/1344745611/original.jpg?aki_policy=profile_x_medium",
	"host_neighbourhood" : "Kailua/Kona",
	"host_listings_count" : 2,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'kba']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Kailua-Kona, Hawaii, United States",
	"neighbourhood_cleansed" : "North Kona",
	"neighbourhood_group_cleansed" : "Hawaii",
	"latitude" : 19.61632,
	"longitude" : -155.98305,
	"property_type" : "Entire place",
	"room_type" : "Entire home/apt",
	"accommodates" : 4,
	"bathrooms" : "",
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : "",
	"amenities" : "[\"Bed linens\", \"TV with standard cable\", \"Washer\", \"Kitchen\", \"Wifi\", \"Hot water\", \"Hangers\", \"Dishes and silverware\", \"Pool\", \"Essentials\", \"Dedicated workspace\", \"Free parking on premises\", \"Coffee maker\", \"Iron\", \"Stove\", \"Cooking basics\", \"Oven\", \"Refrigerator\", \"Dryer\", \"Long term stays allowed\", \"Cable TV\"]",
	"price" : "$169.00",
	"minimum_nights" : 30,
	"maximum_nights" : 120,
	"minimum_minimum_nights" : 30,
	"maximum_minimum_nights" : 30,
	"minimum_maximum_nights" : 120,
	"maximum_maximum_nights" : 120,
	"minimum_nights_avg_ntm" : 30,
	"maximum_nights_avg_ntm" : 120,
	"calendar_updated" : "",
	"has_availability" : "t",
	"availability_30" : 0,
	"availability_60" : 22,
	"availability_90" : 30,
	"availability_365" : 120,
	"calendar_last_scraped" : "2021-12-11",
	"number_of_reviews" : 7,
	"number_of_reviews_ltm" : 0,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2017-01-02",
	"last_review" : "2020-01-06",
	"review_scores_rating" : 3.83,
	"review_scores_accuracy" : 3.67,
	"review_scores_cleanliness" : 3.17,
	"review_scores_checkin" : 4.33,
	"review_scores_communication" : 4,
	"review_scores_location" : 4.83,
	"review_scores_value" : 3.83,
	"license" : "",
	"instant_bookable" : "f",
	"calculated_host_listings_count" : 1,
	"calculated_host_listings_count_entire_homes" : 1,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 0.12
}
{
	"_id" : ObjectId("6245ed7421f2b8ef609bca60"),
	"" : 0,
	"id" : 5269,
	"listing_url" : "https://www.airbnb.com/rooms/5269",
	"scrape_id" : NumberLong("20211211051353"),
	"last_scraped" : "2021-12-12",
	"name" : "Upcountry Hospitality in the 'Auwai Suite",
	"description" : "The 'Auwai Suite is a lovely, self-contained apartment at the back of our historic Waimea Guest House built in the 1800's. This suite is named for the 100-year-old Hawaiian irrigation canal that runs through the property. <br /><br />It has a full kitchen, dining area, beautifully tiled bathroom, bedroom with queen bed and two window seats, a shared back lanai, and a private outdoor table and chairs. <br />This is a most popular suite in Waimea Guest House and is great for extended stays.<br /><br /><b>The space</b><br />The ‘Auwai Suite is a lovely, self-contained apartment at the back of Waimea Guest House. It has a full kitchen, dining area, and beautifully tiled bathroom, as well as a large bedroom - with high vaulted ceilings, a queen bed, and two window seats - that opens out onto a shared back lanai. <br /><br />To find the entrance to this unit, guests follow the traditional Hawaiian ‘auwai (irrigation ditch) that runs along the property towards the back. The most private of th",
	"neighborhood_overview" : "We are located on the \"sunny side\" of Waimea, just off the Kawaihae Road.  Our home is tucked into a quiet residential neighborhood at the base of the Kohala mountain range.",
	"picture_url" : "https://a0.muscache.com/pictures/5b52b72f-5a09-4218-a0c8-ec581f872a35.jpg",
	"host_id" : 7620,
	"host_url" : "https://www.airbnb.com/users/show/7620",
	"host_name" : "Lea & Pat",
	"host_since" : "2009-02-09",
	"host_location" : "Waimea, Hawaii, United States",
	"host_about" : "Lea, born and raised on the Island of Hawaii, just returned with her husband, Pat. We think Waimea is the very best place to live -- central, a little cooler and surrounded by an adorable town.  We offer Hawaiian hospitality to travelers who are looking for an authentic island experience.  We love the Big Island and know it well. The best part of hosting is getting to share tips and tricks with our guests and make sure they see the real deal while staying with us.  ",
	"host_response_time" : "within a few hours",
	"host_response_rate" : "86%",
	"host_acceptance_rate" : "46%",
	"host_is_superhost" : "t",
	"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/16ac6af1-4484-45ec-929b-5fcae8fdce66.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/pictures/user/16ac6af1-4484-45ec-929b-5fcae8fdce66.jpg?aki_policy=profile_x_medium",
	"host_neighbourhood" : "Island of Hawaiʻi",
	"host_listings_count" : 2,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'offline_government_id', 'kba', 'selfie', 'government_id', 'identity_manual']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Kamuela, Hawaii, United States",
	"neighbourhood_cleansed" : "South Kohala",
	"neighbourhood_group_cleansed" : "Hawaii",
	"latitude" : 20.0274,
	"longitude" : -155.702,
	"property_type" : "Entire rental unit",
	"room_type" : "Entire home/apt",
	"accommodates" : 2,
	"bathrooms" : "",
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 1,
	"amenities" : "[\"Bed linens\", \"Shared hot tub\", \"TV with standard cable\", \"Kitchen\", \"Fire extinguisher\", \"Wifi\", \"Hot water\", \"Hangers\", \"Pack \\u2019n play/Travel crib\", \"Dishes and silverware\", \"BBQ grill\", \"Free street parking\", \"Children\\u2019s books and toys\", \"Essentials\", \"Breakfast\", \"Patio or balcony\", \"Backyard\", \"Beach essentials\", \"Dedicated workspace\", \"Smoke alarm\", \"Baking sheet\", \"Luggage dropoff allowed\", \"Shower gel\", \"Coffee maker\", \"Iron\", \"Hair dryer\", \"Babysitter recommendations\", \"Stove\", \"Cooking basics\", \"Oven\", \"Refrigerator\", \"Extra pillows and blankets\", \"Outdoor furniture\", \"Long term stays allowed\", \"Cable TV\"]",
	"price" : "$149.00",
	"minimum_nights" : 3,
	"maximum_nights" : 200,
	"minimum_minimum_nights" : 3,
	"maximum_minimum_nights" : 5,
	"minimum_maximum_nights" : 200,
	"maximum_maximum_nights" : 200,
	"minimum_nights_avg_ntm" : 3.8,
	"maximum_nights_avg_ntm" : 200,
	"calendar_updated" : "",
	"has_availability" : "t",
	"availability_30" : 0,
	"availability_60" : 0,
	"availability_90" : 0,
	"availability_365" : 193,
	"calendar_last_scraped" : "2021-12-12",
	"number_of_reviews" : 16,
	"number_of_reviews_ltm" : 6,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2011-05-31",
	"last_review" : "2021-10-23",
	"review_scores_rating" : 4.53,
	"review_scores_accuracy" : 4.87,
	"review_scores_cleanliness" : 4.27,
	"review_scores_checkin" : 5,
	"review_scores_communication" : 4.87,
	"review_scores_location" : 5,
	"review_scores_value" : 4.8,
	"license" : "119-269-5808-01R",
	"instant_bookable" : "f",
	"calculated_host_listings_count" : 2,
	"calculated_host_listings_count_entire_homes" : 2,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 0.12
}
{
	"_id" : ObjectId("6245ed7421f2b8ef609bca61"),
	"" : 1,
	"id" : 5387,
	"listing_url" : "https://www.airbnb.com/rooms/5387",
	"scrape_id" : NumberLong("20211211051353"),
	"last_scraped" : "2021-12-12",
	"name" : "Hale Koa Studio & 1 Bedroom Units!!",
	"description" : "This Wonderful Spacious Studio apt/flat is in a duplex building has peaceful cottage setting on a working farm in South Kona farm belt rural area , Its elevation provides cool temperatures & amazing lush foliage with ocean and mountain view with cable TV and free wifi.<br />The rural Captain Cook/Honaunau area offers rural charm and comfort, conveniently located off HWY 11 Belt Road.<br /><br /><b>The space</b><br />Hale Koa Duplex:<br />This duplex has a wonderful, peaceful cottage setting and it's elevation provides cool temperatures & amazing, lush foliage. Truly stunning! with cable and free wireless internet service.<br />The structure offers two unique very private spaces with private Entries, Full kitchen with cooking utensils, range, appliances in each unit (see photos), plus free Wi-fi available thru out the space, inside the apt and Lanai.<br /><br />    The FIRST unit is a spacious studio Apt. unit with Queen size bed  in the living room area plus a sleeper-sofa in the front",
	"neighborhood_overview" : "IN a Farm belt area with small commercial farming of coffee, avocados, tropical fruit and macadamia nut trees. Tropical lush nature in peaceful tranquil location with ocean and mountain view and amazing sunsets.",
	"picture_url" : "https://a0.muscache.com/pictures/1170713/dca6af5f_original.jpg",
	"host_id" : 7878,
	"host_url" : "https://www.airbnb.com/users/show/7878",
	"host_name" : "Edward",
	"host_since" : "2009-02-13",
	"host_location" : "Captain Cook, Hawaii, United States",
	"host_about" : "Kona Hawaii,\n \n Ed is a Farmer/Designer \n\nWe are friendly, open minded , Adventurous and creative ,who love sports, travel and explorer our precious globe.\n\nWe enjoy simple minimalist clean interiors and Architecture, Good Healthy food and friendly stylish venues. \n\nAs hosts, we are here if you need us, We certainly won't disturb our guests, if you prefer privacy. \nEach  building has its own private entrance,  you will feel like you're in your home-away-from-home.\n We take our Airbnb hosting responsibilities seriously, and aim to make your visit to The Big Island of Hawaii as comfortable, and enjoyable as possible! ",
	"host_response_time" : "within an hour",
	"host_response_rate" : "100%",
	"host_acceptance_rate" : "100%",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/b895b9d9-e59c-42c9-980c-63808ac90324.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/pictures/user/b895b9d9-e59c-42c9-980c-63808ac90324.jpg?aki_policy=profile_x_medium",
	"host_neighbourhood" : "Kailua/Kona",
	"host_listings_count" : 2,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone', 'reviews', 'kba']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Captain Cook, Hawaii, United States",
	"neighbourhood_cleansed" : "South Kona",
	"neighbourhood_group_cleansed" : "Hawaii",
	"latitude" : 19.43081,
	"longitude" : -155.88069,
	"property_type" : "Entire rental unit",
	"room_type" : "Entire home/apt",
	"accommodates" : 2,
	"bathrooms" : "",
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 1,
	"amenities" : "[\"Bed linens\", \"TV with standard cable\", \"Washer\", \"Kitchen\", \"Microwave\", \"Keypad\", \"Wifi\", \"Wine glasses\", \"Hot water\", \"Hangers\", \"Dishes and silverware\", \"Essentials\", \"Toaster\", \"Dedicated workspace\", \"Smoke alarm\", \"Free parking on premises\", \"Coffee maker\", \"Iron\", \"Hair dryer\", \"Stove\", \"Cooking basics\", \"Oven\", \"Refrigerator\", \"Dryer\", \"Private entrance\", \"Hot water kettle\", \"Extra pillows and blankets\", \"Dishwasher\", \"Dining table\", \"Long term stays allowed\", \"Cable TV\"]",
	"price" : "$85.00",
	"minimum_nights" : 5,
	"maximum_nights" : 60,
	"minimum_minimum_nights" : 5,
	"maximum_minimum_nights" : 5,
	"minimum_maximum_nights" : 26,
	"maximum_maximum_nights" : 1125,
	"minimum_nights_avg_ntm" : 5,
	"maximum_nights_avg_ntm" : 1120,
	"calendar_updated" : "",
	"has_availability" : "t",
	"availability_30" : 2,
	"availability_60" : 6,
	"availability_90" : 9,
	"availability_365" : 253,
	"calendar_last_scraped" : "2021-12-12",
	"number_of_reviews" : 186,
	"number_of_reviews_ltm" : 18,
	"number_of_reviews_l30d" : 2,
	"first_review" : "2010-02-16",
	"last_review" : "2021-11-25",
	"review_scores_rating" : 4.65,
	"review_scores_accuracy" : 4.66,
	"review_scores_cleanliness" : 4.45,
	"review_scores_checkin" : 4.84,
	"review_scores_communication" : 4.88,
	"review_scores_location" : 4.73,
	"review_scores_value" : 4.76,
	"license" : "",
	"instant_bookable" : "t",
	"calculated_host_listings_count" : 2,
	"calculated_host_listings_count_entire_homes" : 2,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 1.29
}
...
```

3. All of the listings offered by both of the two hosts 7620 and 7984 (who are superhosts)

Even though they are superhosts, each of them only have 2 listings. Price of Lea $ Pat is around 150 bucks and price of Ahlea is around 400 bucks.

```
let filter = {"host_id": {$in:[7620,7984]},"host_is_superhost": "t"};
let fields = { _id:0, "name":1, "price":1, "neighborhood":1 , "host_name":1, "host_is_superhost":1};
db.listings.find(filter, fields).pretty()
```
```
{
	"name" : "Upcountry Hospitality in the 'Auwai Suite",
	"host_name" : "Lea & Pat",
	"host_is_superhost" : "t",
	"price" : "$149.00"
}
{
	"name" : "Kauai  Ocean View 3 Story Tiki Tower Princeville",
	"host_name" : "Ahlea",
	"host_is_superhost" : "t",
	"price" : "$425.00"
}
{
	"name" : "Brazilian Pepper Suite",
	"host_name" : "Lea & Pat",
	"host_is_superhost" : "t",
	"price" : "$125.00"
}
...
```

4. All the unique `host_name` values

There are hosts whose names are written in Chinese characters at the very last part of this output 

```
db.listings.distinct("host_name")
```
```
[
	"(Email hidden by Airbnb)",
	"(Super Host)Dennis",
	"A"
	...
]
```

5. All of the places that have more than 2 `beds` in a neighborhood of `Princeville, Hawaii, United States`, ordered by `review_scores_rating` descending

If one wants an airbnb in Princeville with more than 2 beds, he generally needs to be able to afford more than 200 bucks per night.

```
let filter1 = {"beds": {$gt:2},"neighbourhood": "Princeville, Hawaii, United States"};
let fields1 = { _id:0, "name":1, "beds":1, "review_scores_rating":1, "price":1};
let orderBy1 = { "review_scores_rating": -1 };
db.listings.find(filter1, fields1).sort(orderBy1).pretty()
```
```
{
	"name" : "Luxurious Quiet Princeville condo in Paradise.",
	"beds" : 5,
	"price" : "$350.00",
	"review_scores_rating" : 5
}
{
	"name" : "NIHILANI PARADISE 1A W/ AC PRINCEVILLE",
	"beds" : 3,
	"price" : "$355.00",
	"review_scores_rating" : 5
}
{
	"name" : "Westin Princeville - 2 bedroom - Kauai",
	"beds" : 4,
	"price" : "$450.00",
	"review_scores_rating" : 5
}
...
```

6. The number of listings per hosts

Most of the hosts only have one listing

```
db.listings.aggregate([
	{$group: {_id: "$host_name", listingCount: {$sum: 1}}}
	])
```
```
{ "_id" : "Nelli And Stepan", "listingCount" : 1 }
{ "_id" : "Sang", "listingCount" : 2 }
{ "_id" : "Kbm", "listingCount" : 2 }
...
```

7. The average review_scores_rating per neighborhood, and only show the ones above a 4, sorted in descending order of rating

There's no need to limit the score, because all neighbourhood in Hawaii has average score above 4, with Pāhala beting the last one with average score 4.17.

```
db.listings.aggregate([
	{$group: {_id: "$neighbourhood", averageRating: {$avg: "$review_scores_rating"}}},
	{$match: {"averageRating": {$gt:4},}},
	{$sort: {"averageRating":-1} }
	])
```
```
{ "_id" : "Molokai, Hawaii, United States", "averageRating" : 5 }
{ "_id" : "Haena, Hawaii, United States", "averageRating" : 5 }
{ "_id" : "Koloa , Hawaii, United States", "averageRating" : 5 }
...
```

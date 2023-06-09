"""There save raw query's for api/v1/foods/."""


QUERY_LIST_FOOD = str(
    """
    SELECT
        "food_foodcategory"."id" AS "pk", 
        "food_foodcategory"."name_ru", 
        "food_foodcategory"."name_en", 
        "food_foodcategory"."name_ch", 
        "food_foodcategory"."order_id",  
        "food_food"."id", 
        "food_food"."category_id", 
        "food_food"."code", 
        "food_food"."internal_code",
        "food_food"."code", 
        "food_food"."internal_code", 
        "food_food"."cost", 
        "food_food"."is_vegan", 
        "food_food"."is_special", 
        "food_food"."is_publish", 
        "food_food"."name_ru", 
        "food_food"."description_ru", 
        "food_food"."description_en", 
        "food_food"."description_ch",  
        "food_food_additional"."from_food_id" 
    FROM "food_foodcategory"
    INNER JOIN "food_food" 
        ON "food_food"."category_id" = "food_foodcategory"."id" 
    LEFT JOIN "food_food_additional" 
        ON "food_food_additional"."to_food_id" = "food_food"."id"
    WHERE "food_food"."is_publish"
    ORDER BY "food_foodcategory"."id" AND "food_food"."id" ASC;
    """
)

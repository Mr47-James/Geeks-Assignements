# The output will be:

    I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)


# Explanation:

  -  The code uses object destructuring to extract name, country, city, and the coordinates lat and lng from the nested location object.

coordinates: [lat, lng] destructures the array [49.2827, -123.1207] into lat and lng.

Then the template literal outputs all the extracted values in the string.

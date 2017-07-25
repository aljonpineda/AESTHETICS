from google.appengine.ext import ndb

class Info(ndb.Model):
    def __init__(self, location, title, info, climate, issues, bottomtext):
        self.location = location
        self.title = title
        self.info = info
        self.climate = climate
        self.issues = issues
        self.bottomtext = bottomtext
    def listString(self, page_id):
        return "<a href='map?page_id=" + str(page_id) + "'>" + self.title + "</a>"

map_list = [
    Info("id = 'Amazon'",
    "The Amazon Rainforest, South America",
    "Deforestation",
    """The Amazon Rainforest resides in a tropical climate, essentially meaning it is hot and humid in nature. The temperature of the Amazon Rainforest has little variation throughout the year. Temperatures usually range between 26 and 31 degrees celsius. On extreme occasions however, temperatures can get as high as 33 degrees celsius. Temperatures mainly stayed reasonable however, due to immensely high humidity, those foreign to the environment can feel like they are being deprived of air. Rainfall is an intrinsic characteristic to the Amazon Rainforest. Throughout the year data yield results with extreme variability in rainfall. Normally, from December to May, rain is plentiful garnering between 220- 320 mm of rainfall. During June to around November however, rainfall can decrease to only about 50 mm of rain. If you are a tourist, you may want to consider going between May and July in order to experience both spectrums of the Amazon Rain Forest. Some note a change in the recent climate of the Amazon. They blame it on excessive deforestation suffering its worst drought in over 100 years back in 2005. If the trend continues, more trees will be cut down for raw materials which leads to carbon dioxide emission due to dying plants. As a result the entire landscape, in terms of climate, would change.""",
    """Rainforests around the world, and the Amazon Rainforest in particular, face a plethora of issues that inhibit them from keeping their natural integrity. One may believe that the only issue that plagues the forest is deforestation. But factors such as greed and the need to monetize of raw materials set a chain reaction for destruction. Many trees are harvested in order for the gain of raw materials present in furniture and building materials and as a result, there is no foundation to hold dirt which kills fish via suffocation. As a result of greed, people from foreign nations illegally steal exotic wildlife and organisms in hopes of making a profit, thus endangering the vast biodiversity of the rainforest. Another issue of overfishing, where unneeded amounts of fish are brought to the market in over-commercialization. As a result, excess spoilage of fish occurs. According to 'RainforestCruises.com,' over 60 percent of fish are lost due to this terrible practice.""",
    """<img src="resources/AmazonText.png" id="location_text">"""
    ),

    Info("id = 'India'",
    "Delhi, India",
    "Overpopulation",
    """<p>India's climate consists of a variety depending on the location. Generally, India has a hot, tropical climate while the northern region is cooler. Summer has very hot temperatures, reaching to a maximum of 45 degrees Celsius (113 degrees Fahrenheit), while winters are cool and dry. Monsoons are frequent during the summer, sometimes causing flooding along rivers. Himalayan mountains in the north prevent cold winds from coming into India, protecting the country from cold winters. The mountain range also traps monsoon winds from leaving the country. The monsoon winds are frequent during the monsoon season, which is one among the five seasons of India: summer, monsoon, autumn, winter, and spring. </p>
    <p>In New Delhi, the capital of India, the summer months of April, May, and June are characterized by very hot days and hot nights with low precipitation and low humidity. The monsoon months of July, August, and September are characterized by hot days and nights with heavy precipitation and very high humidity. The autumn months of October and November are characterized by warm days and pleasant nights with low precipitation and moderate humidity. The winter months of December and January are characterized by cool days and nights with low precipitation and moderate humidity. The spring months of February and March are characterized by pleasant days and cool nights with low to moderate precipitation and low to moderate humidity.</p>""",
    """India's population is a whopping 1.2 billion and is expected to rise to 1.8 billion at around 2050. Overpopulation adversely affects the country's health issues as water and air pollution levels continue to rise because of crowdedness. Infrastructure is struggling to keep up as less and less services are made available for India's citizens. This includes transportation, healthcare, education, and housing. Overconsumption is a prime byproduct of overpopulation, and this puts natural resources, food, and drinking water at risk to being rapidly depleted. Land for food are being over-exploited, and ground pollution levels will also severely increase. The country's overpopulation also brings with it economic inequality and unemployment since there are not enough jobs to handle the unrestricted population growth rate.""",
    """<img src="resources/IndiaText.png" id="location_text">"""),

    Info("id = 'London'",
    "London, Great Britain",
    "Air Pollution",
    """London has an oceanic, temperate climate, its weather largely affected by the ocean surrounding the island. Temperatures are fair during the summer and cool during the winter. It rarely falls below freezing, and snow is rare. However, rainfall is fairly regular throughout the year. Like in many countries in the northern hemisphere, London has the four seasons of summer, fall, winter, and spring. The summer months of June, July, and August are characterized by warm days and cool nights with moderate precipitation. August is the warmest month. The autumn months of September, October, and November are characterized by cool days and nights with moderate to high precipitation. This season tends to have the most rainfall, October being the wettest month of the year. The winter months of December, January, and February are characterized by cool days and cold nights with moderate precipitation. January is the coolest month. Temperatures, however, do not go lower than freezing. The spring months of March, April, and May are characterized by pleasant days and cool nights with moderate precipitation. Temperatures get higher as the season approaches summer.""",

    """London suffers from air pollution every year, killing thousands of people who are mostly unaware of the deadly air they breathe every day. The city's smog levels reached a record high the January of 2017, even higher than Beijing's air pollution. The pollution is so severe that the mayor, Sadiq Khan, strongly urged children to wear gas masks. And while the smog that enveloped the city in 1952 was clearly visible, the poisonous air of today is invisible, a gas known as nitrogen dioxide or NO2. Aside from the mayor's gas mask suggestion, the government is mostly hesitant to deal with the problem itself since they do not want to restrict the citizens' use of cars, the cause of the city's air pollution. However, the mayor continues to alert the city about the severity of the situation. For instance, in June of 2017, Khan issued an emergency throughout London, having signs by the road flash warnings about the toxic air that will be coming from the south. This is one of the effects that the government is taking to attempt to handle the situation. But currently, London is still blanketed by the invisible gas that would continue to risk citizens of stroke, heart attack, and lung disease.""",
    """<img src="resources/LondonText.png" id="location_text">"""),

    Info("id = 'Sahara'",
    "The Sahara Desert, Africa",
    "Desertification",
    """The Sahara Desert sports on of the harshest climates in the world. The highest temperature ever recorded by meteorologists was 136 degrees fahrenheit on September 13th, 1922 in Azizia, Libya. However normal temperatures during summertime can go as high as 100 degrees fahrenheit. There is huge variability in climate when it comes to evening. Temperatures can drop up to 40 degrees later into the night. During the winter, temperatures can go into the freezing territory in the Northern Sahara wear temperatures can be bearable in the Southern Sahara. In extreme cases, snow may fall on higher altitude points however rarely if not never reaches the desert itself. The Sahara being infamous for sweltering temperatures, is also known for its wind. The Sahara produces torrential winds which can reach hurricane speeds. As a result, it gives birth to sandstorms. To refer to rainfall, the Sahara barely gets any. In some areas there would be no rain for a couple of years, followed by a downpour, and then no rain for several years again. However the norm is usually less than a few inches per year.""",

    """The Sahara Desert faces numerous issues that could lead the biome into ruins. There is a plethora of precious minerals present in Africa's soil and as a result, leads to potassium cyanide left in the soil which essentially poisons the soil, plants and animals within the vicinity.  Another issue that cripples the Sahara is global warming. Global warming, a steady increase of overall temperature due to greenhouse gases present in the atmosphere, can cause droughts throughout the entire Sahara region. It can dry up places with water which can lead to plants and animals consuming an inadequate amount of liquid necessary to survival. And to elaborate on a larger scale, it destroys some part of the food chain. Without the survival of plants, herbivorous creatures would also die out decreasing diversity within the area. The region also serves as a dump for fossil fuels and raw materials which again, will be lethal to the habitat of animals.""",
    """<img src="resources/SaharaText.png" id="location_text">"""),

    Info("id = 'Reef'", "The Great Barrier Reef", "Global Warming",
    """The climate of the Great Barrier Reef is very pleasant and fair throughout the year. With a humid, tropical climate, the Great Barrier Reef’s weather is characterized by warm breezes and moderate to high humidity. Precipitation depends on the season, which is one of two things: winter, or the dry season, and summer, or the wet season. The winter months from May to October have low precipitation and provide sunshine. The summer months from November to April have heavy precipitation and occasional thunderstorms. Swimming is not a problem year round, but the best conditions are during the dry season, between April to October, when box jellyfish do not inhabit the area. Seawater is warm ranging from 23 degrees Celsius to 29 degrees Celsius (73 degrees Fahrenheit to 84 degrees Fahrenheit), so swimming would be pleasant.""",
    """<p>The Great Barrier Reef can be seen from outer space and is the world's biggest single structure made by living organisms. This reef structure is composed of and built by billions of tiny organisms, known as coral polyps. It supports a wide diversity of life and was selected as a World Heritage Site in 1981. CNN labelled it one of the seven natural wonders of the world.</p><p>The Great Barrier Reef supports the world's largest collection of coral reefs, with 400 types of coral, 1,500 species of fish and 4,000 types of mollusc. It also holds great scientific interest as the habitat of species such as the dugong ('sea cow') and the large green turtle, which are threatened with extinction.</p><p>Huge sections of the Great Barrier Reef, stretching across hundreds of miles of its most pristine northern sector, were recently found to be dead, killed last year by overheated seawater. More southerly sections around the middle of the reef that barely escaped then are bleaching now, a potential precursor to another die-off that could rob some of the reef's most visited areas of color and life.</p><p>The damage to the Great Barrier Reef, one of the world's largest living structures, is part of a global calamity that has been unfolding intermittently for nearly two decades and seems to be intensifying. In the paper, dozens of scientists described the recent disaster as the third worldwide mass bleaching of coral reefs since 1998, but by far the most widespread and damaging.</p>""",
    """<img src="resources/ReefText.png" id="location_text">"""),

    Info("id = 'Arctic'",
    "Arctic Ocean",
    "Ice Loss",
    """The climate of the Arctic Ocean is mostly consistent, with cool temperatures during the summer and cold temperatures during the winter. Precipitation is light, and the Arctic Basin can be classified as a desert because of its dryness. Much of the climate is affected by the amount of solar radiation the region receives. During the summer, the sun remains above the horizon for a whole 24 hours, offering the area warm temperatures up to around 10 degrees Celsius (50 degrees Fahrenheit). Some land areas even reach 30 degrees Celsius (86 degrees Fahrenheit). Following summer, the autumn months of September and October show rapid transition of shorter days. Solar radiation lessens, and temperatures drop with it. By November, the beginning of winter, any solar radiation remaining does not affect the climate. By now, sea ice refreezes and receives a snow cover, which reflects any sunlight back into the atmosphere. The winter is largely characterized by darkness and frigid weather. Any time when the sun does rise above the horizon does not affect the climate. It is not until March, the beginning of spring, when the days rapidly transition to having longer sunshine hours. Much of the snow melts, and the land under it warms up.""",
    """Over the years, both Antarctica and the Arctic Ocean suffer from ice declines, and recently, between the 10th and 12th of June, a large iceberg about the size of Delaware broke off from Antarctica. The diminishing ice may indicate signs of global warming, but some scientists believe that the actual cause is "natural variability." In other words, Antarctica's climate has variations to the extent that it does not remain cold for some ice to stay at certain times of the year. For example, in late 2016, a set of storms brought down warm winds that caused ice the size of South Carolina to break off and melt. Regardless of whether it is natural variability or global warming, the fact remains that sea levels rise by 0.35 mm per year according to NASA. They also reported that between 2002 to 2016, ice had been declining at a rate of 125 gigatons per year. These changes may have drastic effects in the far future, but changes could be made to slow down the raising of sea level, including the reduction of fossil fuel usage. If global warming is the ultimate cause of ice loss, then controlling CO2 emissions can help lessen the net sea level rise."""
    "<img src='resources/AntarcticaText.png' id='location_text'>")
]

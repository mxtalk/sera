# p1 Geodetic datum

p2 *City of Chicago Datum Benchmark*

p3 A geodetic datum or geodetic system (also: geodetic reference datum, geodetic reference system, or geodetic reference frame, or terrestrial reference frame) is a global datum reference or reference frame for unambiguously representing the position of locations on Earth by means of either geodetic coordinates (and related vertical coordinates) or geocentric coordinates.[1] Datums[note 1] are crucial to any technology or technique based on spatial location, including geodesy, navigation, surveying, geographic information systems, remote sensing, and cartography. A horizontal datum is used to measure a horizontal position, across the Earth's surface, in latitude and longitude or another related coordinate system. A vertical datum is used to measure the elevation or depth relative to a standard origin, such as mean sea level (MSL). A three-dimensional datum enables the expression of both horizontal and vertical position components in a unified form.[2] The concept can be generalized for other celestial bodies as in planetary datums.

p4 Since the rise of the global positioning system (GPS), the ellipsoid and datum WGS 84 it uses has supplanted most others in many applications. The WGS 84 is intended for global use, unlike most earlier datums. Before GPS, there was no precise way to measure the position of a location that was far from reference points used in the realization of local datums, such as from the Prime Meridian at the Greenwich Observatory for longitude, from the Equator for latitude, or from the nearest coast for sea level. Astronomical and chronological methods have limited precision and accuracy, especially over long distances. Even GPS requires a predefined framework on which to base its measurements, so WGS 84 essentially functions as a datum, even though it is different in some particulars from a traditional standard horizontal or vertical datum.

p5 A standard datum specification (whether horizontal, vertical, or 3D) consists of several parts: a model for Earth's shape and dimensions, such as a reference ellipsoid or a geoid; an origin at which the ellipsoid/geoid is tied to a known (often monumented) location on or inside Earth (not necessarily at 0 latitude 0 longitude); and multiple control points or reference points that have been precisely measured from the origin and physically monumented. Then the coordinates of other places are measured from the nearest control point through surveying. Because the ellipsoid or geoid differs between datums, along with their origins and orientation in space, the relationship between coordinates referred to one datum and coordinates referred to another datum is undefined and can only be approximated. Using local datums, the disparity on the ground between a point having the same horizontal coordinates in two different datums could reach kilometers if the point is far from the origin of one or both datums. This phenomenon is called datum shift or, more generally, datum transformation, as it may involve rotation and scaling, in addition to displacement.

p6 Because Earth is an imperfect ellipsoid, local datums can give a more accurate representation of some specific area of coverage than WGS 84 can. OSGB36, for example, is a better approximation to the geoid covering the British Isles than the global WGS 84 ellipsoid.[3] However, as the benefits of a global system often outweigh the greater accuracy, the global WGS 84 datum has become widely adopted.[4]

## p7 History

p8 *The Great Trigonometrical Survey of India, one of the first surveys comprehensive enough to establish a geodetic datum.*

p9 The spherical nature of Earth was known by the ancient Greeks, who also developed the concepts of latitude and longitude, and the first astronomical methods for measuring them. These methods, preserved and further developed by Muslim and Indian astronomers, were sufficient for the global explorations of the 15th and 16th Centuries.

p10 However, the scientific advances of the Age of Enlightenment brought a recognition of errors in these measurements, and a demand for greater precision. This led to technological innovations such as the 1735 Marine chronometer by John Harrison, but also to a reconsideration of the underlying assumptions about the shape of Earth itself. Isaac Newton postulated that the conservation of momentum should make Earth oblate (wider at the equator than the corresponding sphere), while the early surveys of Jacques Cassini (1720) led him to believe Earth was prolate (narrower at the equator). The subsequent French geodesic missions (1735-1739) to Lapland and Peru corroborated Newton, but also discovered variations in gravity that would eventually lead to the geoid model.

p11 A contemporary development was the use of the trigonometric survey to accurately measure distance and location over great distances. Starting with the surveys of Jacques Cassini (1718) and the Anglo-French Survey (1784–1790), by the end of the 18th century, survey control networks covered France and the United Kingdom. More ambitious undertakings such as the Struve Geodetic Arc across Eastern Europe (1816-1855) and the Great Trigonometrical Survey of India (1802-1871) took much longer, but resulted in more accurate estimations of the shape of the Earth ellipsoid. The first triangulation across the United States was not completed until 1899.

p12 The U.S. survey resulted in the North American Datum (horizontal) of 1927 (NAD 27) and the Vertical Datum of 1929 (NAVD29), the first standard datums available for public use. This was followed by the release of national and regional datums over the next several decades. Improving measurements, including the use of early satellites, enabled more accurate datums in the later 20th century, such as NAD 83 in North America, ETRS89 in Europe, and GDA94 in Australia. At this time global datums were also first developed for use in satellite navigation systems, especially the World Geodetic System (WGS 84) used in the U.S. global positioning system (GPS), and the International Terrestrial Reference System and Frame (ITRF) used in the European Galileo system.

## p13 Dimensions

### p14 Horizontal datum

p15 A horizontal datum is a model used to precisely measure positions on Earth; it is thus a crucial component of any spatial reference system or map projection. A horizontal datum binds a specified reference ellipsoid, a mathematical model of the shape of the earth, to the physical earth. Thus, the geographic coordinate system on that ellipsoid can be used to measure the latitude and longitude of real-world locations. Regional horizontal datums, such as NAD 27 and NAD 83, usually create this binding with a series of physically monumented geodetic control points of known location. Global datums, such as WGS 84 and ITRF, are typically bound to the center of mass of the Earth (making them useful for tracking satellite orbits and thus for use in satellite navigation systems.

p16 A specific point can have substantially different coordinates, depending on the datum used to make the measurement. For example, coordinates in NAD 83 can differ from NAD 27 by up to several hundred feet. There are hundreds of local horizontal datums around the world, usually referenced to some convenient local reference point. Contemporary datums, based on increasingly accurate measurements of the shape of Earth, are intended to cover larger areas. The WGS 84 datum, which is almost identical to the NAD 83 datum used in North America and the ETRS89 datum used in Europe, is a common standard datum.[citation needed]

### p17 Vertical datum

p18 A vertical datum is a reference surface for vertical positions, such as the elevations of Earth features including terrain, bathymetry, water level, and human-made structures.

p19 An approximate definition of sea level is the datum WGS 84, an ellipsoid, whereas a more accurate definition is Earth Gravitational Model 2008 (EGM2008), using at least 2,159 spherical harmonics. Other datums are defined for other areas or at other times; ED50 was defined in 1950 over Europe and differs from WGS 84 by a few hundred meters depending on where in Europe you look. Mars has no oceans and so no sea level, but at least two martian datums have been used to locate places there.

## p20 Geodetic coordinates

p21 *The same position on a spheroid has a different angle for latitude depending on whether the angle is measured from the normal line segment CP of the ellipsoid (angle α) or the line segment OP from the center (angle β). The "flatness" of the spheroid (orange) in the image is greater than that of Earth; as a result, the corresponding difference between the "geodetic" and "geocentric" latitudes is also exaggerated.*

p22 In geodetic coordinates, Earth's surface is approximated by an ellipsoid, and locations near the surface are described in terms of geodetic latitude ($\phi$), longitude ($\lambda$), and ellipsoidal height ($h$).[note 2]

## p23 Earth reference ellipsoid

p24 The ellipsoid is completely parameterised by two geometric parameters, for example, the semi-major axis $a$ and the flattening $f$.

| p25 Parameter | Symbol |
|---|---|
| p26 Semi-major axis | $a$ |
| p27 Reciprocal of flattening | $\frac{1}{f}$ |

p28 From $a$ and $f$ it is possible to derive the semi-minor axis $b$, first eccentricity $e$ and second eccentricity $e'$ of the ellipsoid

| p29 Parameter | Value |
|---|---|
| p30 Semi-minor axis | $b = a(1 - f)$ |
| p31 First eccentricity squared | $e^2 = 1 - \frac{b^2}{a^2} = f(2 - f)$ |
| p32 Second eccentricity squared | ${e'}^2 = \frac{a^2}{b^2} - 1 = \frac{f(2 - f)}{(1 - f)^2}$ |

p33 The two main reference ellipsoids used worldwide are the GRS 80,[5] recommended by the IERS for use with the ITRF, and the WGS 84,[6] used in the Global Positioning System (GPS).

p34 *GRS 80 parameters*

| p35 Parameter | Notation | Value |
|---|---|---|
| p36 Semi-major axis | $a$ | 6378137 m |
| p37 Reciprocal of flattening | $\frac{1}{f}$ | 298.257222101 |

p38 *WGS 84 defining parameters*

| p39 Parameter | Notation | Value |
|---|---|---|
| p40 Semi-major axis | $a$ | 6378137.0 m |
| p41 Reciprocal of flattening | $\frac{1}{f}$ | 298.257223563 |

p42 *WGS 84 derived geometric parameters*

| p43 Parameter | Notation | Value |
|---|---|---|
| p44 Semi-minor axis | $b$ | 6356752.3142 m |
| p45 First eccentricity squared | $e^2$ | 6.69437999014×10−3 |
| p46 Second eccentricity squared | ${e'}^2$ | 6.73949674228×10−3 |

## p47 Datum transformation

p48 The difference in co-ordinates between datums is commonly referred to as datum shift. The datum shift between two particular datums can vary from one place to another within one country or region, and can be anything from zero to hundreds of meters (or several kilometers for some remote islands). The North Pole, South Pole and Equator will be in different positions on different datums, so True North will be slightly different. Different datums use different interpolations for the precise shape and size of Earth (reference ellipsoids). For example, in Sydney there is a 200 metres (700 feet) difference between GPS coordinates configured in GDA (based on global standard WGS 84) and AGD (used for most local maps), which is an unacceptably large error for some applications, such as surveying or site location for scuba diving.[7]

p49 Datum conversion is the process of converting the coordinates of a point from one datum system to another. Because the survey networks upon which datums were traditionally based are irregular, and the error in early surveys is not evenly distributed, datum conversion cannot be performed using a simple parametric function. For example, converting from NAD 27 to NAD 83 is performed using NADCON (later improved as HARN), a raster grid covering North America, with the value of each cell being the average adjustment distance for that area in latitude and longitude. Datum conversion may frequently be accompanied by a change of map projection.

## p50 Discussion and examples

p51 A geodetic reference datum is a known and constant surface which is used to describe the location of unknown points on Earth. Since reference datums can have different radii and different center points, a specific point on Earth can have substantially different coordinates depending on the datum used to make the measurement. There are hundreds of locally developed reference datums around the world, usually referenced to some convenient local reference point. Contemporary datums, based on increasingly accurate measurements of the shape of Earth, are intended to cover larger areas. The most common reference Datums in use in North America are NAD 27, NAD 83, and WGS 84.

p52 The North American Datum of 1927 (NAD 27) is "the horizontal control datum for the United States that was defined by a location and azimuth on the Clarke spheroid of 1866, with origin at (the survey station) Meades Ranch (Kansas)." ... The geoidal height at Meades Ranch was assumed to be zero, as sufficient gravity data was not available, and this was needed to relate surface measurements to the datum. "Geodetic positions on the North American Datum of 1927 were derived from the (coordinates of and an azimuth at Meades Ranch) through a readjustment of the triangulation of the entire network in which Laplace azimuths were introduced, and the Bowie method was used."[8] NAD 27 is a local referencing system covering North America.

p53 The North American Datum of 1983 (NAD 83) is "The horizontal control datum for the United States, Canada, Mexico, and Central America, based on a geocentric origin and the Geodetic Reference System 1980 (GRS 80). "This datum, designated as NAD 83…is based on the adjustment of 250,000 points including 600 satellite Doppler stations which constrain the system to a geocentric origin." NAD 83 may be considered a local referencing system.

p54 WGS 84 is the World Geodetic System of 1984. It is the reference frame used by the U.S. Department of Defense (DoD) and is defined by the National Geospatial-Intelligence Agency (NGA) (formerly the Defense Mapping Agency, then the National Imagery and Mapping Agency). WGS 84 is used by the DoD for all its mapping, charting, surveying, and navigation needs, including its GPS "broadcast" and "precise" orbits. WGS 84 was defined in January 1987 using Doppler satellite surveying techniques. It was used as the reference frame for broadcast GPS Ephemerides (orbits) beginning January 23, 1987. At 0000 GMT January 2, 1994, WGS 84 was upgraded in accuracy using GPS measurements. The formal name then became WGS 84 (G730), since the upgrade date coincided with the start of GPS Week 730. It became the reference frame for broadcast orbits on June 28, 1994. At 0000 GMT September 30, 1996 (the start of GPS Week 873), WGS 84 was redefined again and was more closely aligned with International Earth Rotation Service (IERS) frame ITRF 94. It was then formally called WGS 84 (G873). WGS 84 (G873) was adopted as the reference frame for broadcast orbits on January 29, 1997.[9] Another update brought it to WGS 84 (G1674).

p55 The WGS 84 datum, within two meters of the NAD 83 datum used in North America, is the only world referencing system in place today. WGS 84 is the default standard datum for coordinates stored in recreational and commercial GPS units.

p56 Users of GPS are cautioned that they must always check the datum of the maps they are using. To correctly enter, display, and to store map related map coordinates, the datum of the map must be entered into the GPS map datum field.

### p57 Examples

p58 Examples of map datums are:

- p59 WGS 84, 72, 66 and 60 of the World Geodetic System
- p60 NAD 83, the North American Datum which is very similar to WGS 84
- p61 NAD 27, the older North American Datum, of which NAD 83 was basically a readjustment [1]
- p62 OSGB36 of the Ordnance Survey of Great Britain
- p63 ETRS89, the European Datum, related to ITRS
- p64 ED50, the older European Datum
- p65 GDA94, the Australian Datum[10]
- p66 JGD2011, the Japanese Datum, adjusted for changes caused by 2011 Tōhoku earthquake and tsunami[11]
- p67 Tokyo97, the older Japanese Datum[12]
- p68 KGD2002, the Korean Datum[13]
- p69 TWD67 and TWD97, different datum currently used in Taiwan.[14]
- p70 BJS54 and XAS80, old geodetic datum used in China[15]
- p71 GCJ-02 and BD-09, Chinese encrypted geodetic datum.
- p72 PZ-90.11, the current geodetic reference used by GLONASS[16]
- p73 Galileo Terrestrial Reference Frame (GTRF), the geodetic reference used by Galileo; currently defined as ITRF2005[17]
- p74 CGCS2000, or CGS-2000, the geodetic reference used by BeiDou Navigation Satellite System; based on ITRF97[17][18][19]
- p75 International Terrestrial Reference Frames (ITRF88, 89, 90, 91, 92, 93, 94, 96, 97, 2000, 2005, 2008, 2014), different realizations of the ITRS.[20][21]
- p76 Hong Kong Principal Datum, a vertical datum used in Hong Kong.[22][23]
- p77 SAD69 - South American Datum 1969

## p78 Plate movement

p79 The Earth's tectonic plates move relative to one another in different directions at speeds on the order of 50 to 100 mm (2.0 to 3.9 in) per year.[24] Therefore, locations on different plates are in motion relative to one another. For example, the longitudinal difference between a point on the equator in Uganda, on the African Plate, and a point on the equator in Ecuador, on the South American Plate, increases by about 0.0014 arcseconds per year.[citation needed] These tectonic movements likewise affect latitude.

p80 If a global reference frame (such as WGS 84) is used, the coordinates of a place on the surface generally will change from year to year. Most mapping, such as within a single country, does not span plates. To minimize coordinate changes for that case, a different reference frame can be used, one whose coordinates are fixed to that particular plate. Examples of these reference frames are "NAD 83" for North America and "ETRS89" for Europe.

## p81 See also

- p82 Axes conventions
- p83 Earth-centered, Earth-fixed coordinate system (ECEF)
- p84 Earth-centered inertial (ECI)
- p85 Datum reference
- p86 Figure of the Earth
- p87 Geoid
- p88 Geographic coordinate conversion
- p89 Projected coordinate system
- p90 International Terrestrial Reference System and Frame
- p91 Kilometre zero
- p92 Local tangent plane coordinates
- p93 Ordnance datum
- p94 Milestone
- p95 Planetary coordinate system
- p96 Frame of reference
- p97 Timeline of Earth estimates
- p98 World Geodetic System

## p99 Footnotes

1. p100 The plural is not "data" in this case.
2. p101 About the right/left-handed order of the coordinates, i.e., $(\lambda, \phi)$ or $(\phi, \lambda)$, see Spherical coordinate system#Conventions.

## p102 References

1. p103 Jensen, John R.; Jensen, Ryan R. (2013). Introductory Geographic Information Systems. Pearson. p. 25.
2. p104 "NOAA/NOS's VDatum: A tutorial on datums". NOAA/NOS's VDatum 4.7. 2014-03-14. Retrieved 2024-08-11.
3. p105 "Geoid—Help". ArcGIS for Desktop. Archived from the original on 2017-02-02. Retrieved 2017-01-23.
4. p106 "Datums—Help". ArcGIS for Desktop. Archived from the original on 2017-02-02. Retrieved 2017-01-23.
5. p107 "Geocentric Datum of Australia Technical Manual" (PDF). Intergovernmental Committee on Surveying and Mapping. 2 December 2014. Archived from the original (PDF) on 2018-03-20. Retrieved 2017-02-20.
6. p108 "NGA: DoD World Geodetic System 1984". Archived from the original on 2017-07-04. Retrieved 2007-03-01.
7. p109 McFadyen. "GPS - An Explanation of How it Works". Michael McFadyen's Scuba Diving Web Site. Archived from the original on 2006-08-19.
8. p110 "National Geodetic Survey - Frequently Asked Questions FAQ".
9. p111 "Frequently Asked Questions". National Geodetic Survey. Archived from the original on 2011-10-19.
10. p112 Craven, Alex. "GDA94 : Frequently Asked Questions". Geoproject Solutions. Archived from the original on 2016-08-15.
11. p113 "日本測地系2011（JGD2011）とは？ - 空間情報クラブ". club.informatix.co.jp. 2015-08-20. Archived from the original on 2016-08-20.
12. p114 "座標変換ソフトウェア TKY2JGD｜国土地理院". www.gsi.go.jp. Archived from the original on 2017-11-05.
13. p115 Yang, H.; Lee, Y.; Choi, Y.; Kwon, J.; Lee, H.; Jeong, K. (2007). "The Korean Datum Change to a World Geodetic System". AGU Spring Meeting Abstracts. 2007: G33B–03. Bibcode:2007AGUSM.G33B..03Y.
14. p116 台灣地圖夢想家-SunRiver. "大地座標系統與二度分帶座標解讀 - 上河文化". www.sunriver.com.tw. Archived from the original on 2016-08-20.
15. p117 Analysis of Conversion Method and Map Merging from BJS54 XA80 Surveying and Mapping Results to CGCS2000 Archived 2016-09-18 at the Wayback Machine
16. p118 "The transition to using the terrestrial geocentric coordinate system "Parametry Zemli 1990" (PZ-90.11) in operating the GLObal NAvigation Satellite System (GLONASS) has been implemented". www.glonass-iac.ru. Archived from the original on 2015-09-07.
17. p119 "Use of international references for GNSS operations and applications" (PDF). unoosa.org. Archived (PDF) from the original on 2017-12-22.
18. p120 Handbook of Satellite Orbits: From Kepler to GPS, Table 14.2
19. p121 BeiDou Navigation Satellite System Signal In Space Interface Control Document, Open Service Signal (Version 2.0) Archived 2016-07-08 at the Wayback Machine section 3.2
20. p122 "Archived copy" (PDF). Archived (PDF) from the original on 2017-01-26. Retrieved 2016-08-19.
21. p123 "General concepts". itrf.ensg.ign.fr. Archived from the original on 2008-12-04.
22. p124 "Vertical Datum used in China – Hong Kong – onshore". Archived from the original on 2012-11-13.
23. p125 "Explanatory Notes on Geodetic Datums in Hong Kong" (PDF). geodetic.gov.hk. Archived from the original (PDF) on 2016-11-09. Retrieved 2016-08-19.
24. p126 Read HH, Watson Janet (1975). Introduction to Geology. New York: Halsted. pp. 13–15.

## p127 Further reading

1. p128 Soffel, Michael; Langhans, Ralf (2012-06-20). "Terrestrial Reference System". Space-Time Reference Systems. Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-642-30226-8_8. ISBN 978-3-642-30225-1. ISSN 0941-7834.
2. p129 Babcock, Alice K.; Wilkins, George A. (1988) The Earth's Rotation and Reference Frames for Geodesy and Geodynamics Springer ISBN 9789027726582
3. p130 List of geodetic parameters for many systems from University of Colorado
4. p131 Gaposchkin, E. M. and Kołaczek, Barbara (1981) Reference Coordinate Systems for Earth Dynamics Taylor & Francis ISBN 9789027712608
5. p132 Kaplan, Understanding GPS: principles and applications, 1 ed. Norwood, MA 02062, USA: Artech House, Inc, 1996.
6. p133 GPS Notes
7. p134 P. Misra and P. Enge, Global Positioning System Signals, Measurements, and Performance. Lincoln, Massachusetts: Ganga-Jamuna Press, 2001.
8. p135 Peter H. Dana: Geodetic Datum Overview – Large amount of technical information and discussion.
9. p136 US National Geodetic Survey

## p137 External links

- p138 GeographicLib includes a utility CartConvert which converts between geodetic and geocentric (ECEF) or local Cartesian (ENU) coordinates. This provides accurate results for all inputs including points close to the center of Earth.
- p139 A collection of geodetic functions that solve a variety of problems in geodesy in Matlab Archived 2020-08-07 at the Wayback Machine.
- p140 NGS FAQ – What is a geodetic datum?
- p141 About the surface of the Earth on kartoweb.itc.nl

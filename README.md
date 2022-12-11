# Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming
<br>
## Predict Clicked Ads Customer Classification by using Machine Learning: Overview <br>
### Some company in Indonesia want to know the effective about some ad that their already publish, this is an important thing for company to know how much this ad can interactive the customer when their look at the ad.<br>
With processing the historical data advertisement, found an insight, and also path that happened, so can help the company to found the target marketing , focus in this case is made a classification machine learning model that can help marketing found the best and accurate customer for the company purpose.<br>
 <br>
## About Dataset : <br>
-	This data have 1000 data,  such as 7 numerics and 5 categoricals. <br>
-	There are some uncompleted data in some columns.<br>
<br>
## EDA<br>
### 1.	Numeric data <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/EDA%20numerik.jpg 'EDA Numeric')
<br>
### -	Daily Time Spent on Site have mean 64.929 and Age 36 years old. <br>
### -	Minimum people usage internet daily is 104.7. <br>
### -	Maximum income people in 5.563. <br>
<br>
### 2.	Categoric data <br>

![ALT](https:https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/EDA%20kategorik.jpg "EDA Categorik")
<br>


### -	Female have many time to surfing in internet. <br>
### -	Surabaya is the most city that get into the internet. <br>
### -	Many people go to automotive section in internet. <br>
<br>
### 3.	Correlation <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/corellation.jpg "Corellation")
<br>

### The correlation between Clicked on Ad and with another columns <br>
### a.	Daily Time Spent on Site 0.74 <br>
### b.	Age 0.49 <br>
### c.	Area indome 0.47 <br>
### d.	Daily Internet Usage 0.79 <br>
### e.	Male 0.02 <br>
### f.	City 0.08 <br>
### g.	Province 0.07 <br>
### h.	Category 0.00 <br>

### 4.	Analysis <br>
### a.	Relationship between Age and Daily Time on Site <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Relationship%20betweet%20daily%20spent%20and%20age.jpg"Relatinship between daily time and age")
<br>
### b.	Relationship between Internet Usage and Age <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Relationship%20between%20daily%20internet%20usage%20and%20age.jpg "Relatinship between Internet Usage and age")
<br>
### c.	Relationship between Internet Usage and Daily Time Spent on Site <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Relationship%20between%20daily%20intenet%20usage%20and%20spent%20on%20site.jpg "Relationship between Daily Time Spent and Internet Usage")
<br>
 
## Data Pre processing <br>
### -	For null data, numeric using mean and categoric use modus. <br>
### -	There’s no duplicated data. <br>
### -	For Timestamp column, there’s a change datatype to date using pandas (pd.to_datetime). After that, the new date column are extracted according to their respective function such as year,month, day, and week. <br>
### -	Future Encoding mapping for male and clicked on Ad. One hot encoding for city, category and province. <br>
### -	Split data 70:30 with data from columns : Daily Time Spent on Site, Age ,Area Income ,Daily Internet Usage, city_Balikpapan, city_Cimahi, city_Jakarta Pusat, city_Malang, city_Serang, city_Tangerang Selatan, province_Banten, province_Jawa Barat, province_Kalimantan Timur, Clikked on ad. Clicked on ad column for the target. <br>

## Modelling <br>
#### This dataset using 5 model, Logistic Regression; Decision Tree; Random Forest; Adaboost; and XGboost. With two different treatment, before and after standardization. <br>
### a.	Before Standardization <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Modelling.jpg "Before standardization")
<br>
### b.	After Standardization <br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/modelling%20after%20standarization.jpg "After standardization")
<br>

### From the result, we used modelling without standardization and for the best modeeling is Adaboost. This is the future Importance from the modelling.
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Future%20importance%20adaboost.jpg "Future Importance")
<br>
The future importance are Area Income, Daily Time Spent on Site. Daily Internet Usage, Age, and City Tanggerang Selatan. <br>
### Form This modelling,  we can calculate the matrix.<br>
![ALT](https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming/blob/main/Fig/Matrix.jpg "Matrix")
<br>
## Results <br>
### The business recommendation are:<br>
### a.	Give a easier access to click for people who in adults until elderly. <br>
### b.	Giving a colour for the clicked so that can make an eye catching and easy. <br>
### c.	Simple instruction for people so they can follow convenient.<br>
### d.	Offer a promotion for province that have a lower consuming surfing internet.<br>
### Result from the Modelling:<br>
### -	Assumption:<br>
### The company conducts a survey to click ads that appear on the website. The sales department conducts a campaign with a cost 30000IDR per customer. If a customner clicks, the company gets 100000 IDR per customer. So the company earns a profit:<br>
 ###Cost : 30000IDR<br>
### Revenue : 100000IDR<br>
### Profit   = Revenue-Cost<br>
###	= 100000IDR-30000IDR<br>
###	= 70000IDR<br>
### If we don’t using the modelling:<br>
### Profit   = (Revenuex1000)-(Costx1000)<br>
###	= (100000IDRx500)-(30000IDRx1000)<br>
###	= 20000000IDR<br>
### If we using the modelling:<br>
### Profit   = (Revenuex1000)-(Costx1000)<br>
###	= (100000IDRx95)-(30000IDRx96)<br>
###	= 6620000IDR<br>
### With using a machine learning, the profit will increase 3.31%.<br>
<br>
For more detail, you can visit the link below:<br>
https://github.com/inggridpris/Predict-Clicked-Ads-Customer-Classification-by-using-Machine-Learming <br>
https://drive.google.com/drive/folders/1bn4pdGtVZAwFSYAYMvSp__vC4BXDzBro?usp=sharing <br>
<br>
or you can connect with me with linkedin <br>
https://www.linkedin.com/in/inggriani-priscilia-69779b179/ <br>


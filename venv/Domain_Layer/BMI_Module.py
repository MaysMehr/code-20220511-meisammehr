import json
import pandas as pd
import numpy as np
from math import floor
import unittest




class BMI():

	df_People = []

	def __init__(self):
		self.df_People = pd.DataFrame([] , columns=["Gender" , "HeightCm" , "WeightKg" ,
		                                       "BMI" , "BMICategory" ,"HealthRisk"])


	def calc_BMI(self , mass:int , height_cm:int):
		"""Calculates the BMI measure for a person by mass and height values
			the unit of height_cm should be changed from cm to m^2

			Parameters
			-----------
			mass : int, mandatory
				   The gender of the person

			height_cm : int , mandatory
				        the height of person in cm
			Returns
            -------
            Float
                the BMI of a person as a Float

			Raises
			------
			Exception
				All parameters should be completed

		"""
		if mass is None or height_cm is None:
			raise Exception("parameters should be completed")

		height_m2 = pow(height_cm/100 , 2)
		calc_bmi_lambda = lambda mass , height2: round(mass / height2 , 2)
		bmi_person = calc_bmi_lambda(mass , height_m2)

		return bmi_person


	def calc_Total_Number_Overweight(self):
		"""Calculates the total number of Overweight perosns

			Returns
            -------
            int
                the number of a Overweight person

		    Raises
			 ------

		"""

		count_Overweight = 0
		count_Overweight = self.df_People.groupby(["BMICategory"])["BMICategory"].count()["Overweight"]

		return count_Overweight


	def get_BMI_Category(self , BMI_range: float):
		"""Returns BMI-Category value and Health-Risk value by BMI

		   Parameters
		   ----------
		   BMI_range : float, mandatory
		           The BMI of the person

		   Returns
           -------
           list
                 a list, conints of BMI-Category value and Health-Risk value

		   Raises
		   ------
		   Exception
		            All parameters should be completed

		"""
		if BMI_range is None:
			raise Exception("parameter should be completed")

		if BMI_range <= 18.40:
			return [{"BMICategory":"Underweight" , "HealthRisk" : "Malnutrition risk"}]
		elif BMI_range >= 18.50 and BMI_range <= 24.90:
			return [{"BMICategory":"Normal weight" , "HealthRisk" : "Low risk"}]
		elif BMI_range >= 25 and BMI_range <= 29.90:
			return [{"BMICategory":"Overweight" , "HealthRisk" : "Enhanced risk"}]
		elif BMI_range >= 30 and BMI_range <= 34.90:
			return [{"BMICategory":"Moderately obese" , "HealthRisk" : "Medium risk"}]
		elif BMI_range >= 35 and BMI_range <= 39.90:
			return [{"BMICategory":"Severely obese" , "HealthRisk" : "High risk"}]
		elif BMI_range >= 40:
			return [{"BMICategory":"Very severely obese" , "HealthRisk" : "Very high risk"}]
		else:
			return [{"BMICategory": "unknown category" , "HealthRisk": "unknown category"}]


	def add_Person_To_Data(self, gender:str=None , height_cm : int =None , weight_kg : int=None):
		"""Adds a new person to the main list People.

		   Parameters
		   ----------
		   gender : str, mandatory
		           The gender of the person

		   height_cm : int , mandatory
		           the height of person in cm

		   weight_kg : int , mandatory
		           the weight of the person in kg

		   Raises
		   ------
		   Exception
		            All parameters should be completed

		"""
		if gender is None or height_cm is None or weight_kg is None:
			raise Exception("parameters should be completed")

		bmi = self.calc_BMI(weight_kg , height_cm)

		bmi_description = self.get_BMI_Category(bmi)[0]
		BMICategory = bmi_description["BMICategory"]
		HealthRisk = bmi_description["HealthRisk"]

		df_new_row = pd.DataFrame([[gender , height_cm , weight_kg , bmi
			, BMICategory , HealthRisk]] , columns=["Gender" , "HeightCm" , "WeightKg" ,
		                                           "BMI" , "BMICategory" , "HealthRisk"]  )

		self.df_People = pd.concat((self.df_People , df_new_row),ignore_index=True)


	def add_Json_Batch_To_Data(self , json_str):
		"""Adds a json of persons to the main list People.

		Parameters
		----------
		json_str : json file , mandatory
				   The json file format to aff the main list

		Raises
		------
		ValueError
			checks the json format that should be correct
		"""
		# try:
		# 	jsonfile = json.loads(json_str)
		# except ValueError as err:
		# 	raise ValueError("the format of json string is not correct")

		jsonfile = json.loads(json_str)
		df_new = pd.DataFrame( jsonfile , columns=["Gender" , "HeightCm" , "WeightKg"])

		for idx,row in df_new.iterrows():
			bmi = self.calc_BMI(row["WeightKg"] , row["HeightCm"])
			bmi_description = self.get_BMI_Category(bmi)[0]
			BMICategory = bmi_description["BMICategory"]
			HealthRisk = bmi_description["HealthRisk"]
			df_new.at[idx , "BMI"] = bmi
			df_new.at[idx , "BMICategory"] = BMICategory
			df_new.at[idx , "HealthRisk" ] = HealthRisk

		self.df_People = pd.concat((self.df_People , df_new) , ignore_index=True)



	def get_All_People_Json(self):
		"""Returns all data of People as a Json

		   Returns
		   ------
		   json
		     the all member of the list People as a Json format

		   Raises
		   ------

		"""
		df = self.df_People
		result = df.to_json(orient="records")
		parsed = json.loads(result)

		return json.dumps(parsed)


	def get_All_People(self):
		"""Returns all data of People as a DataFrame

		   Returns
		   ------
		   list
		     the all member of the list People as a DataFrame

		   Raises
		   ------

		"""
		return self.df_People

	def test1(self):
		return 123


import unittest
import Domain_Layer.BMI_Module as BM

class Test_BMI(unittest.TestCase):

	def test_calc_BMI_1(self):
		obj = BM.BMI()
		actual = obj.calc_BMI(75 , 175)
		expected = 24.49
		self.assertEqual(actual , expected)

	# def test_calc_BMI_2_Parameter_None(self):
	# 	obj = BM.BMI()
	# 	actual = obj.calc_BMI(75  , 175)     # one of paameteres would be None
	# 	expected = 24.49
	# 	self.assertEqual( str(exception_context.exception) , "parameters should be completed")

	def test_calc_BMI_2(self):
		obj = BM.BMI()
		actual = obj.calc_BMI(75 , 175)   # pne of parameters is not sent
		expected = 24.49
		self.assertEqual(actual , expected)

	def test_get_BMI_Category(self):
		obj = BM.BMI()
		actual = obj.get_BMI_Category( 37.5 )
		expected = [{"BMICategory":"Severely obese" , "HealthRisk" : "High risk"}]
		self.assertEqual(actual , expected)



if __name__ == '__main__':
    unittest.main()


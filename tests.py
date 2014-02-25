from unittest import TestCase

from datetime import date

from main import *


class MySuperBigTestCase(TestCase):

    def testParseDateWillRejectMiddleTermFourDigit(self):
	# if you put year in the middle you're crazy! it's either
	# left or right
        self.assertFalse(is_valid_date('02/2008/13'))

    def testIsLeftyWilleReturnTrueIfWereSureThatYearIsOnTheLeft(self):
    	self.assertTrue(is_lefty('2008/12/03'))

    def testIsLeftyWillReturnFalseIfWereSureThatYearIsOnTheRight(self):
        self.assertFalse(is_lefty('03/10/2004'))

    def testIsLeftyWillReturnNoneIfCannotDecide(self):
        self.assertIsNone(is_lefty('03/12/05'))

    def testRotateWillReturnSameTupleIfDryrunIsTrue(self):
        self.assertEquals((1, 2, 3), rotate((1, 2, 3), dryrun=True))

    def testRotateWillReturnRotatedTupleIfDryrunIsFalse(self):
        self.assertEquals((1, 2, 3, 4, 5), rotate((5, 4, 3, 2, 1), dryrun=False))

    def testChooseEarlierWillReturnEarlierDate(self):
        d1 = date(2001, 10, 10)
        d2 = date(2003, 10, 2)
        self.assertEqual(d1, earlier_date(d1, d2))

    def testParseAsSafestDateWillActuallyParseAsSafestDate(self):
        self.assertEquals(date(2001, 2, 13), as_safest_date('01/02/13'))
        self.assertEquals(date(2001, 2, 13), as_safest_date('2001/02/13'))
        self.assertEquals(date(2001, 2, 13), as_safest_date('13/02/2001'))
        self.assertEquals(date(2013, 2, 1), as_safest_date('2013/02/01'))
        self.assertEquals(date(2013, 2, 1), as_safest_date('01/02/2013'))

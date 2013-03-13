import unittest
import math

import numpy

from pyrr import matrix33
from pyrr import matrix44
from pyrr import quaternion
from pyrr import vector3


class test_matrix44( unittest.TestCase ):

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_create_identity( self ):
        result = matrix44.create_identity()

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 identity incorrect"
            )

    def test_create_from_translation( self ):
        translation = numpy.array( [ 2.0, 3.0, 4.0 ] )
        mat = matrix44.create_from_translation( translation )
        result = mat[ 3, 0:3 ]

        expected = translation

        # translation goes down the last column in normal matrix
        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 translation not set properly"
            )

    def test_create_from_scale( self ):
        scale = numpy.array( [ 2.0, 3.0, 4.0 ] )

        mat = matrix44.create_from_scale( scale )

        result = mat.diagonal()[ :-1 ]

        expected = scale

        # extract the diagonal scale and ignore the last value
        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 scale not set properly"
            )

    def test_create_matrix33_view( self ):
        mat = matrix44.create_identity()
        result = matrix44.create_matrix33_view( mat )

        expected = numpy.eye( 3 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 create_matrix33_view incorrect"
            )

    def test_create_from_matrix33( self ):
        mat = matrix33.create_identity()
        result = matrix44.create_from_matrix33( mat )

        expected = numpy.eye( 4 )

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Matrix44 create_from_matrix33 incorrect"
            )

    def test_create_from_quaternion( self ):
        def identity():
            quat = quaternion.create_identity()
            result = matrix44.create_from_quaternion( quat )

            expected = numpy.eye( 4 )

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix44 from quaternion incorrect with identity quaternion"
                )
        identity()

        def rotated_x():
            quat = quaternion.create_from_x_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_x_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about X"
                )
        rotated_x()

        def rotated_y():
            quat = quaternion.create_from_y_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_y_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about Y"
                )
        rotated_y()

        def rotated_z():
            quat = quaternion.create_from_z_rotation( math.pi )
            result = matrix44.create_from_quaternion( quat )

            expected = matrix44.create_from_z_rotation( math.pi )

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 from quaternion incorrect with PI rotation about Z"
                )
        rotated_z()

    def test_apply_to_vector( self ):
        def identity():
            mat = matrix44.create_identity()
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = vec

            self.assertTrue(
                numpy.array_equal( result, expected ),
                "Matrix44 apply_to_vector incorrect with identity"
                )
        identity()

        def rotated_x():
            mat = matrix44.create_from_x_rotation( math.pi )
            vec = vector3.unit.y

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about X"
                )
        rotated_x()

        def rotated_y():
            mat = matrix44.create_from_y_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about Y"
                )
        rotated_y()

        def rotated_z():
            mat = matrix44.create_from_z_rotation( math.pi )
            vec = vector3.unit.x

            result = matrix44.apply_to_vector( mat, vec )

            expected = -vec

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with rotation about Y"
                )
        rotated_z()

        def translation():
            mat = matrix44.create_identity()
            vec = numpy.array([0.0, 0.0, 0.0])
            mat[3,0:3] = [1.0, 2.0, 3.0]

            result = matrix44.apply_to_vector( mat, vec )

            expected = mat[3,0:3]

            self.assertTrue(
                numpy.allclose( result, expected ),
                "Matrix44 apply_to_vector incorrect with translation"
                )
        translation()
    
if __name__ == '__main__':
    unittest.main()

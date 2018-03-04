import argparse

from math import acos, degrees

# argpare

def get_parsed_args():
    """
    Gives parsed arguments from command line.

    :returns: argparse.Namespace with parsed arguments
    """
    parser = argparse.ArgumentParser(
        usage="For count the angles of a triangle",

        description="This function counts the angles of a triangle if 3 sides are known",
        )

    # ==================================
    # Arguments for parsing command line
    # ==================================

    parser.add_argument('-a', '--a_side', 
                        type=int,
                        metavar='',
                        required=True, 
                        help='a-side of the triangle'
                        )
    parser.add_argument('-b', '--b_side', 
                        type=int,
                        metavar='',
                        required=True, 
                        help='b-side of the triangle'
                        )
    parser.add_argument('-c','--c_side', 
                        type=int,
                        metavar='',
                        required=True, 
                        help='c-side of the triangle'
                        )
    
    return parser.parse_args()

def dtriangle(a, b, c):
    """
    Count count the angles of a triangle

    :returns: list of integers (degrees)
    """

    # Warning if you input a wrong side that it's can't be a triangle
    warn = "It's can't be a triangle!"

    try:
        A = round(degrees(acos((pow(b, 2)+pow(c, 2)-pow(a,2))/(2*b*c))))
        B = round(degrees(acos((pow(a, 2)+pow(c, 2)-pow(b,2))/(2*a*c))))
        C = round(degrees(acos((pow(b, 2)+pow(a, 2)-pow(c,2))/(2*b*a))))

        if A == 0 or B == 0  or C == 0:
            return warn
        else:
            return [A, B, C]
    except ValueError:
        return warn


if __name__ == '__main__':
    parsed_args = get_parsed_args()
    print(dtriangle(parsed_args.a_side, parsed_args.b_side, parsed_args.c_side))
    # dtriangle(3,4,5)
    # dtriangle(5,4,3)
    # dtriangle(10,20,30)
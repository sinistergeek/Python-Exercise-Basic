from pymonad import Curry
@curry
def systolic_bp(bmi,age,gender_male,treatment):
    return(
        68.15 + 0.58*bmi+0.65*age+0.94*gender_male+6.44*treatment
    )

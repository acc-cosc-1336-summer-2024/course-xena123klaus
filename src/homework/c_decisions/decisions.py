def get_options_ratio(option, total):
    return option / total

def get_faculty_rating(ratio):
    if ratio >=.9 and ratio < 1:
        return "Excellent" 
    elif ratio > .8:
        return "Very Good"
    elif ratio > .7:
        return "Good"
    elif ratio > .6:
        return "Needs Improvement"
    elif 0 <= ratio <= .59:
        return "Unacceptable"
    else:
        return "Error"
    

    

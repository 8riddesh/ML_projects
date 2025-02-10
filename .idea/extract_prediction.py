import get_Data as gt
def extract_answer():
    ans=gt.get_data(False)
    if ans==1:
        return 'Non-Diabetics'
    else:
        return 'Diabetics'

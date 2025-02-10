import pickle


def get_data():
    try:
        bmi = int(input('Enter BMI: '))
        phyHlt = int(input('Enter days health not good out of 30: '))
        age = int(input('Age: '))
        highbp = int(input('High BP (1/0): '))
        highcol = int(input('High cholesterol (1/0): '))
        smoker = int(input('Smoker (1/0): '))
        fruits = int(input('Eat fruits (1/0): '))
        veggies = int(input('Eat veggies (1/0): '))
        HvyAlcoholConsump = int(input('Heavy alcohol consumption (1/0): '))
        GenHlt = int(input('General health (0 to 4): '))
        gender = int(input('Gender (1 for male, 0 for female): '))

        input_list = [bmi, phyHlt, age, highbp, highcol, smoker, fruits, veggies, HvyAlcoholConsump, GenHlt, gender]

        with open('Model/Diabetic_model.pkl', 'rb') as f:
            model = pickle.load(f)

        value = model.predict([input_list])
        return (value[0], input_list)

    except ValueError as e:
        print("Invalid input, please enter valid numbers.")
    except FileNotFoundError as e:
        print("Model file not found. Please ensure 'Diabetic_model.pkl' is in the correct directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

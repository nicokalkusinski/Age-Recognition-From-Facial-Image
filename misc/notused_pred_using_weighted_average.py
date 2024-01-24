def get_weighted_pred_age(actual_age: int, accuracy_list: list, predicted_ages: list) -> list:
    """calculated the weighted predicted age of the person basing on accuracies and prediction of the models

    Args:
        actual_age (int): actual age of the person in the picture
        accuracy_list (list): accuracies provided by the models used
        predicted_ages (list): predicted ages provided by the models used

    Returns:
        list: [actual age, weighted predicted age, difference between the two as number, difference between the two as percent]
    """
    if len(accuracy_list) == len(predicted_ages) and actual_age >= 0:
        rel_total = sum(accuracy_list) #summing the accs so they sum up to be 100% of the accuracy.

        #calculating the relative weights assigned to each of the model basing on their accuracy
        rel_weights = []
        for acc in accuracy_list: rel_weights.append(acc/rel_total)

        #using predicted age by each of the model and its accuracy to calculate the end prediction.
        weighted_pred_ages = []
        for i, age in enumerate(accuracy_list):
            weighted_pred_ages.append(rel_weights[i]*predicted_ages[i])
        
        #getting the weighted prediction and the difference between the actual and predicted
        predicted_age = sum(weighted_pred_ages)
        difference_num = abs(actual_age - predicted_age)
        difference_percent = abs(difference_num/actual_age)*100

        return [actual_age, predicted_age, difference_num, difference_percent]
    else:
        print("arguments requirements not matched.")
        return []

accs = [0.93, 0.57, 0.76, 0.83] #example accuraccies produced by 4 different models
# pred_ages = [36, 43, 40, 31] #predicted age by those 4 different models
for i in range(20, 41, 2):
    pred_ages = [i-1, i+6, i+3, i-6] #make it random diverse
    actual_age = i #the actual age of the person in the picture
    outcome = get_weighted_pred_age(actual_age, accs, pred_ages)
    print(f"Actual age: {outcome[0]}")
    print(f"Predic age: {outcome[1]:.2f}")
    print(f"Difference: {outcome[2]:.2f} ({outcome[3]:.2f}%)")
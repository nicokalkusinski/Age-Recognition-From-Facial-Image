def show_prediction(vis, DATADIR, predictor, filename):
    """show real time prediction on the picture of your choice

    Args:
        vis (ktrain.vision): vision object imported from ktrain library
        DATADIR (folder): folder with a specific structure to use ktrain
        predictor (kt.predictor): predictor object made of the learner (model) and preproc data
        filename (string): name of the file. e.g. 34_76.jpg
    """
    actual_age = int(filename.split("_")[0])
    path = f"{DATADIR}/test/{actual_age}/{filename}"
    predicted_age = int(predictor.predict_filename(path)[0])
    
    diff = abs(actual_age-predicted_age)
    
    vis.show_image(path)
    
    print(f"Predicted age: {predicted_age}")
    print(f"Actual age: {actual_age}")
    print(f"Difference: {diff} year(s), {(diff/actual_age)*100:.2f}%")

def grading_sample_accuracy(DATADIR, grading_sample_path, predictor) -> None:
    """assess accuracy based on the grading sample. Mostly used with the training.

    Args:
        DATADIR (folder): folder with images of specific structure for ktrain
        grading_sample_path (path): path to the grading_sample.txt
        predictor (predictor): predictor object made by ktrain.get_predictor()
    """
    with open(grading_sample_path, "r") as f:
        gs = f.read().split(",")
    
    results = []
    for image in gs:
        actual_age = int(image.split("_")[0])
        path = f"{DATADIR}/test/{actual_age}/{image}"
        predicted_age = int(predictor.predict_filename(path)[0])
        
        diff = abs(actual_age-predicted_age)
        results.append([actual_age, predicted_age, diff, (diff/actual_age)*100])

    # Loop through each inner list and sum the second values
    avg_error = 0
    avg_perror = 0
    for age_diff in results:
        avg_error += age_diff[2]
        avg_perror += age_diff[3]
    avg_error /= 100
    avg_perror /=100
    print(avg_error, "years(s)", avg_perror, "%")
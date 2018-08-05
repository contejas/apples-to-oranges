def answer(test_path):
    import time
    t0 = time.time()

    from learning import process_test_data, training_data, training_answers
    from sklearn.neighbors import KNeighborsClassifier

    test_data = process_test_data(test_path)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(training_data, training_answers)

    ans = knn.predict(test_data)
    t1 = time.time()
    return [ans, t1 - t0]
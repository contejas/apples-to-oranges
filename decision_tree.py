def answer(test_path):
    import time
    t0 = time.time()

    from learning import process_test_data, training_data, training_answers
    from sklearn import tree

    test_data = process_test_data(test_path)

    clf = tree.DecisionTreeClassifier()
    clf.fit(training_data, training_answers)

    ans = clf.predict(test_data)
    t1 = time.time()
    return [ans, t1 - t0]
def answer(test_path):
    import time
    t0 = time.time()

    from learning import process_test_data, training_data, training_answers
    from sklearn.linear_model.logistic import LogisticRegression

    test_data = process_test_data(test_path)

    lr = LogisticRegression()
    lr.fit(training_data, training_answers)

    ans = lr.predict(test_data).item()
    t1 = time.time()
    return [ans, t1 - t0]
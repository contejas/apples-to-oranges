def answer(test_path):

    import warnings
    warnings.filterwarnings("ignore")

    import time
    t0 = time.time()

    from learning import process_test_data, training_data, training_answers
    from sklearn.cluster.k_means_ import KMeans
    from sklearn.linear_model.logistic import LogisticRegression

    test_data = process_test_data(test_path)

    km = KMeans()
    km.fit(training_data, training_answers)

    myNum = km.predict(test_data).item()

    numX = [1, 2, 4, 2, 7, 0, 2, 7, 4, 3, 2, 1, 4, 5, 5, 1, 3, 0, 4, 2]
    numbers = [[num] for num in numX]
    letX = ['a', 'a', 'o', 'a', 'o', 'o', 'a', 'a', 'o', 'a', 'a', 'o', 'a', 'o', 'o', 'o', 'a', 'a', 'o', 'a']
    letters = [[letter] for letter in letX]

    lr = LogisticRegression()
    lr.fit(numbers, letters)

    ans = lr.predict(myNum).item()

    t1 = time.time()
    return [ans, t1 - t0]

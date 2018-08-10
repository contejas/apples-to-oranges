import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import time

class Public_Variable_Storage():
    def __init__(self):
        self.img_path = None
        self.final_char = None
        self.algorithm = None
        self.timing = None

    def setImgPath(self, fpath):
        self.path = fpath
    def getImgPath(self):
        return self.path

    def setFinalChar(self, fChar):
        self.final_char = fChar
    def getFinalChar(self):
        return self.final_char

    def setAlgorithm(self, algor):
        self.algorithm = algor
    def getAlgorithm(self):
        return self.algorithm

    def setTime(self, t):
        self.timing = str(t)
    def getTime(self):
        return self.timing

public = Public_Variable_Storage()

login = tk.Tk()
loginframe = tk.Frame(login)
login.title("Welcome to Apples-to-Oranges! ")

tk.Label(login, text="Hello! This program takes in a picture and decides whether the picture looks").grid()
tk.Label(login, text="more like an apple or an orange based on the colors presented in the image.").grid()

def final_verdict():
    algo.destroy()
    verdict = tk.Tk()
    vFrame = tk.Frame(verdict)
    verdict.title("Is it an apple or an orange?")
    tk.Label(verdict, text="Your image is an...").grid()
    if public.getFinalChar() == "o":
        f = "Orange!"
        col = "orange"
    elif public.getFinalChar() == "a":
        f = "Apple!"
        col = "red"
    else:
        f = "Undecided! The program could not comprehend your image."
        col = "blue"
    tk.Label(verdict, text=f, fg=col, font=('Comic Sans MS',30)).grid()
    tk.Label(verdict, text="Using a " + public.getAlgorithm() + " algorithm, the program").grid()
    tk.Label(verdict, text="trained and tested data to come up with an answer in").grid()
    tk.Label(verdict, text=str(public.getTime()) + " seconds!").grid()
    tk.Button(verdict, text="Exit", command=exit).grid()


def chooseAlgorithm():
    login.destroy()
    global algo
    algo = tk.Tk()
    algoframe = tk.Frame(algo)
    algo.title("Choose an Algorithm")

    tk.Label(algo, text="Please choose an algorithm for the AI to use! More will be added!")

    def decision_tree():
        public.setAlgorithm("Decision Tree")
        tk.Label(algo, text="Loading... Please Wait...").grid()
        time.sleep(2)
        from algorithms import decision_tree
        ans = decision_tree.answer(public.getImgPath())
        public.setFinalChar(ans[0])
        public.setTime(ans[1])
        final_verdict()

    def kn_neighbors():
        public.setAlgorithm("K-Nearest Neighbors")
        tk.Label(algo, text="Loading... Please Wait...").grid()
        time.sleep(2)
        from algorithms import k_nearest_neighbors
        ans = k_nearest_neighbors.answer(public.getImgPath())
        public.setFinalChar(ans[0])
        public.setTime(ans[1])
        final_verdict()

    def log_regression():
        public.setAlgorithm("Logistic Regression")
        tk.Label(algo, text="Loading... Please Wait...").grid()
        time.sleep(2)
        from algorithms import logistic_regression
        ans = logistic_regression.answer(public.getImgPath())
        public.setFinalChar(ans[0])
        public.setTime(ans[1])
        final_verdict()

    def neural_net():
        public.setAlgorithm("Neural Network")
        tk.Label(algo, text="Loading... Please Wait...").grid()
        time.sleep(2)
        from algorithms import neural_network
        ans = neural_network.answer(public.getImgPath())
        public.setFinalChar(ans[0])
        public.setTime(ans[1])
        final_verdict()

    def k_means():
        public.setAlgorithm("K-Means Clustering")
        tk.Label(algo, text="Loading... Please Wait...").grid()
        time.sleep(2)
        from algorithms import k_means_clustering
        ans = k_means_clustering.answer(public.getImgPath())
        public.setFinalChar(ans[0])
        public.setTime(ans[1])
        final_verdict()

    tk.Button(algo, text="Decision Tree", command=decision_tree).grid()
    tk.Button(algo, text="K-Nearest Neighbors", command=kn_neighbors).grid()
    tk.Button(algo, text="Logistic Regression", command=log_regression).grid()
    tk.Button(algo, text="Neural Network", command=neural_net).grid()
    tk.Button(algo, text="K-Means Clustering", command=k_means).grid()
    algo.mainloop()


def getImage():
    public.setImgPath(filedialog.askopenfilename(initialdir = "/",title = "Please select a picture of an apple, orange, or whatever! Make sure its a JPG, JPEG, or PNG file.")) # File must be a .jpg or .jpeg
    if public.getImgPath():
        confirm = tk.Toplevel()
        confirmframe = tk.Frame(confirm)
        confirm.title("This is your picture?")
        tk.Label(confirm, text="Is this the picture that you want to use?").grid()
        img = ImageTk.PhotoImage(Image.open(public.getImgPath()).resize((300, 300), Image.ANTIALIAS))
        tk.Label(confirm, image=img, height=200).grid()

        def yes():
            confirm.destroy()
            tk.Button(login, text="Choose ML Algorithm to parse data.", command=chooseAlgorithm).grid()

        def no():
            confirm.destroy()
            getImage()

        tk.Button(confirm, text="Yes", command=yes).grid(row=1, column=1)
        tk.Button(confirm, text = "No", command=no).grid(row=1, column=2)
        confirm.mainloop()

tk.Button(login, text="Choose image to have the AI process", command=getImage).grid()
tk.Button(login, text="Exit", command=login.destroy).grid()
login.mainloop()
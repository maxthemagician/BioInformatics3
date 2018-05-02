import re
import math

class NaiveBayes:


    def __init__(self, filename_training):
        """read in the trainings dataset and store the sum of feature variants according to the feauture number and classification"""
        self.proportion = [0] * 2
        for i in range(2):
            self.proportion[i] = [0] * 401

        self.file = filename_training
        file_training = open(filename_training, "r")

        for line in file_training:

            sample = re.split(r'\t+', line)
            interaction = int(sample[0])
            self.proportion[interaction][0] = (self.proportion[interaction][0]) + 1

            for index, feature in enumerate(sample):
                if index != 0:
                    i = (index-1) * 4 + (int(feature)+1)
                    self.proportion[interaction][i] = self.proportion[interaction][i] + 1

    def predict_given_features(self, sample):
        """ predicts the state of the proteins (complex/no complex) given a list of features"""
        total_interaction = float(self.proportion[1][0])
        total_no_interaction = float(self.proportion[0][0])
        total = total_interaction + total_no_interaction

        sum_p = 0.0
        for index, feature in enumerate(sample):
            if index != 0:

                i = (index-1) * 4 + (int(feature)+1)
                feature_interaction = float(self.proportion[1][i])
                feature_no_interaction = float(self.proportion[0][i])
                total = feature_interaction + feature_no_interaction
                if (total != 0) & (feature_no_interaction != 0) & (feature_interaction != 0):
                    sum_p = sum_p + math.log((feature_interaction / total_interaction) / (feature_no_interaction / total_no_interaction))


        return sum_p + math.log((total_interaction/total) / (total_no_interaction/total))


    def test(self, filename_test):
        """read in test dataset, perform classification and check predicted classification"""
        file_test = open(filename_test, "r")

        result = []
        accuracy = 0.0
        total = 0
        for line in file_test:
            total = total + 1
            sample = re.split(r'\t+', line)
            classified = self.predict_given_features(sample)
            if ((classified > 0) & (int(sample[0])) == 1) | ((classified <= 0) & (int(sample[0]) == 0)):
                accuracy = accuracy + 1
                if classified > 0:
                    result.append([1, "true"])
                else:
                    result.append([0, "true"])

            else:
                if classified > 0:
                    result.append([1, "false"])
                else:
                    result.append([0, "false"])

        print(accuracy/total)
        return result

    def find_highest_log_ratio(self):
        """ return the 10 highest absolute log-ratio values and prints them with their respective feature number and variante"""
        max_ration = [-1] * 10
        feature_var = [[0,0]] * 10
        total_interaction = float(self.proportion[1][0])
        total_no_interaction = float(self.proportion[0][0])
        counter_ = 0

        for index, feature in enumerate(self.proportion[0]):

            if index != 0:
                ratio_0 = math.log((float(self.proportion[1][index]) / total_interaction)/(float(self.proportion[0][index])/total_no_interaction))
                ratio_0 = math.fabs(ratio_0)

                if ratio_0 > min(max_ration):
                    i = max_ration.index(min(max_ration))
                    max_ration[i] = ratio_0
                    feature_var[i] = [[counter_, ((index - counter_ - 1)/4)]]

                counter_ = counter_ + 1
                if counter_ > 3:
                    counter_ = 0

        print feature_var + max_ration
        return max_ration

if __name__ == "__main__":
        bayes = NaiveBayes("C:\Users\CarolinM\Desktop\BioInf\\training1.tsv")
        NaiveBayes.find_highest_log_ratio(bayes)
        NaiveBayes.test(bayes, "C:\Users\CarolinM\Desktop\BioInf\\test1.tsv")

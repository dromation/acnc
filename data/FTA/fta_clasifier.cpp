#include <iostream>
#include <vector>
#include <map>

using namespace std;

// Define a structure for the failure catalog
struct Failure {
    string name;
    string description;
    double probability;
};

// Define a structure for the cause catalog
struct Cause {
    string name;
    string description;
    vector<Failure*> failures;
};

// Define a structure for the effect catalog
struct Effect {
    string name;
    string description;
    vector<Cause*> causes;
};

class FaultTreeClassifier {
public:
    // Add a failure to the failure catalog
    void add_failure(string name, string description, double probability) {
        Failure* failure = new Failure;
        failure->name = name;
        failure->description = description;
        failure->probability = probability;
        failures[name] = failure;
    }

    // Add a cause to the cause catalog
    void add_cause(string name, string description, vector<string> failure_names) {
        Cause* cause = new Cause;
        cause->name = name;
        cause->description = description;
        for (auto name : failure_names) {
            if (failures.find(name) != failures.end()) {
                cause->failures.push_back(failures[name]);
            }
        }
        causes[name] = cause;
    }

    // Add an effect to the effect catalog
    void add_effect(string name, string description, vector<string> cause_names) {
        Effect* effect = new Effect;
        effect->name = name;
        effect->description = description;
        for (auto name : cause_names) {
            if (causes.find(name) != causes.end()) {
                effect->causes.push_back(causes[name]);
            }
        }
        effects[name] = effect;
    }

    // Classify an effect by recursively computing the probability of all causes
    double classify(string effect_name) {
        double probability = 1.0;
        if (effects.find(effect_name) != effects.end()) {
            Effect* effect = effects[effect_name];
            for (auto cause : effect->causes) {
                double cause_probability = 1.0;
                for (auto failure : cause->failures) {
                    cause_probability *= (1.0 - failure->probability);
                }
                cause_probability = 1.0 - cause_probability;
                probability *= cause_probability;
            }
            probability = 1.0 - probability;
        }
        return probability;
    }

private:
    map<string, Failure*> failures;
    map<string, Cause*> causes;
    map<string, Effect*> effects;
};

int main() {
    FaultTreeClassifier classifier;

    // Add failures to the failure catalog
    classifier.add_failure("failure1", "Failure 1 description", 0.1);
    classifier.add_failure("failure2", "Failure 2 description", 0.2);
    classifier.add_failure("failure3", "Failure 3 description", 0.3);

    // Add causes to the cause catalog
    classifier.add_cause("cause1", "Cause 1 description", {"failure1", "failure2"});
    classifier.add_cause("cause2", "Cause 2 description", {"failure1", "failure3"});

    // Add effects to the effect catalog
    classifier.add_effect("effect1", "Effect 1 description", {"cause1", "cause2"});

    // Classify an effect
    double probability = classifier.classify("effect1");
    cout << "Probability of effect1: " << probability << endl;

    return 0;
}

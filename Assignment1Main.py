import ExtractGraph
import BeamSearch

# Extract graph from assign1_sentences.txt.
graph = ExtractGraph.ExtractGraph()
# Test extraction correctness.
head_word = "<s>"
tail_word = "Water"
print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
head_word = "Water"
tail_word = "<s>"
print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
head_word = "planned"
tail_word = "economy"
print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
head_word = "."
tail_word = "</s>"
print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is "
				+  str(graph.getProb(head_word, tail_word)))

# Find the sentence with highest probability using basic beam search.
beam_search = BeamSearch.BeamSearch(graph)
sentence_prob = beam_search.beamSearch("<s>", 10, 20)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)
sentence_prob = beam_search.beamSearch("<s> Israel and Jordan signed the peace", 10, 40)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)
sentence_prob = beam_search.beamSearch("<s> It is", 10, 15)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)


# Find the sentence with highest probability using beam search with sentence length-normalzation.
lambda = 0.7
beam_search = BeamSearch.BeamSearch(graph)
sentence_prob = beam_search.beamSearch("<s>", 10, lambda, 20)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)
sentence_prob = beam_search.beamSearch("<s> Israel and Jordan signed the peace", 10, lambda, 40)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)
sentence_prob = beam_search.beamSearch("<s> It is", 10, lambda, 15)
print(str(sentence_prob.score) + "\t" + sentence_prob.string)
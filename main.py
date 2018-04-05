import jsonpickle, pickle

f = open(r'msvd_vid1_rcnn.pkl', 'rb')
D = pickle.load(f, encoding='iso-8859-1')
frozen = jsonpickle.encode(D)

f = open(r'msvd_vid1_rcnn.json', 'w')
f.write(frozen)
f.close()
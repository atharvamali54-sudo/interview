# 🎯 Java Interview Quick Revision (मराठी नोट्स)

हे नोट्स वाचून तुम्ही Internshala किंवा कोणत्याही कंपनीच्या Java AI / Technical Interview मध्ये अगदी आत्मविश्वासाने उत्तरे देऊ शकता.

---

## 📌 १. ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग (OOPs Concepts)

इंटरव्ह्यूमध्ये विचारतात: *"What are the 4 pillars of OOPs?"*

1. **Encapsulation (डेटा सुरक्षित ठेवणे):**
   * Class मधील variables `private` ठेवणे आणि त्यांना access करण्यासाठी `public` getter आणि setter methods वापरणे.
   * **उदा:** बँक खात्यातील बॅलन्स थेट कोणीही बदलू नये म्हणून getter/setter द्वारेच व्यवहार करणे.

2. **Inheritance (कोड पुन्हा वापरणे):**
   * एका Parent class ची वैशिष्ट्ये Child class मध्ये वापरणे (`extends` keyword).
   * **उदा:** `Vehicle` (Parent) -> `Car` (Child).

3. **Polymorphism (एकाच गोष्टीचे अनेक रूपे):**
   * **Method Overloading:** एकाच class मध्ये एकाच नावाची method, पण arguments वेगळे (Compile-time).
   * **Method Overriding:** Parent class मधील method Child class मध्ये बदलून नवीन logic देणे (`@Override` - Runtime).

4. **Abstraction (केवळ महत्त्वाचे दाखवणे, अंतर्गत कोड लपवणे):**
   * कार चालवताना आपल्याला स्टेअरिंग आणि ब्रेक दिसतो, पण इंजिन आत कसे फिरते ते लपवले जाते. हे `Interface` किंवा `Abstract class` ने साध्य होते.

---

## 📌 २. वारंवार विचारले जाणारे महत्त्वाचे प्रश्न (FAQ)

### प्रश्न १: `==` आणि `.equals()` मध्ये काय फरक आहे?
* **साधे उत्तर:**
  * `==` हे दोन्ही गोष्टींची **मेमरी जागा (Address)** तपासते.
  * `.equals()` हे दोन्ही गोष्टींमधील **मजकूर (Content / Value)** तपासते.

### प्रश्न २: String ही Immutable का आहे?
* एकदा String तयार केल्यावर ती बदलता येत नाही. बदल करायचा असल्यास मेमरीमध्ये नवीन String object तयार होतो.
* **फायदा:** सुरक्षितता (Security), Thread Safety आणि String Constant Pool मधील मेमरी बचत.

### प्रश्न ३: ArrayList vs LinkedList
* **ArrayList:** शोधण्यासाठी (Search / Random Access) वेगवान आहे, कारण ती index वर चालते.
* **LinkedList:** नवीन डेटा टाकण्यासाठी किंवा काढण्यासाठी (Insertion / Deletion) वेगवान आहे, कारण यात pointer बदलले जातात.

### प्रश्न ४: Exception Handling मध्ये `try`, `catch`, `finally`
* `try`: ज्या कोडमध्ये त्रुटी (Exception) येण्याची शक्यता असते तो कोड यात ठेवतात.
* `catch`: त्रुटी आल्यास काय करायचे ते यात हाताळले जाते.
* `finally`: हा block **नेहमी चालतो** (फायली बंद करण्यासाठी किंवा डेटाबेस कनेक्शन बंद करण्यासाठी).

---

## 💡 AI Interview मधील महत्त्वाच्या टिप्स:
1. **शांत राहा आणि स्पष्ट बोला:** AI तुमचे बोलणे (Speech) ट्रॅक करत असतो. अडखळत बोलण्यापेक्षा साधे आणि स्पष्ट बोला.
2. **Keywords वापरा:** उदा. Polymorphism सांगताना *Overloading* आणि *Overriding* हे शब्द आलेच पाहिजेत.
3. **इंग्रजीत उत्तर देण्याचा प्रयत्न करा:** जर पूर्ण वाक्य जमत नसेल, तर लहान वाक्ये वापरा:
   * *"Encapsulation means binding data and code together."*
   * *"String is immutable because once created, it cannot be changed."*

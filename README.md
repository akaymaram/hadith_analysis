


# hadith_analysis
Creating a graph-based encoding of the chain of narrations in  کتاب سُليم بن قيس الهلالي

Graph theory, particularly social network analysis, can be used to analyze Hadith by modeling the "sanad" (chain of narrators) as a network, allowing for the study of network properties and the identification of prominent narrators, potentially aiding in hadith authentication.

1.
Running manabeh_generator.py with the csv output file name as a command line argument
generates the first 25 manabeh from the manabeh list.
Example:
python3 manabeh_generator.py manabeh.csv
generates manabeh.csv in the same directory of this script with the first 25 manabeh



Next Steps:
1. make the edges directed
2.check the below links
Al-Ahadeeth: A Visualization Tool of the Hadiths’ Chain of Narrators
https://link.springer.com/chapter/10.1007/978-3-031-61953-3_1

gist.github.com/rvanbruggen/a6e2e80a6fa7a253f46de9fbe9ce361f

Backlog:
1. Build a daily screenshot job using Mac Automator or crontab
2. Fix the manabe_generator.py to include all sources not just the first 25 elements in the manabeh list
3. Expand the ETL of manabeh data to include all books with under 100 entries
4. Check the references and cited by in Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD paper in https://doi.org/10.1016/j.dib.2024.110439

reading backlog:
stats.meta.stackexchange.com/questions/2010/markdown-link-not-being-rendered-as-a-hyperlink


references
Extraction and Visualization of the Chain of Narrators from Hadiths using ***Named Entity Recognition*** and Classification
https://www.dline.info/jcl/fulltext/v5n1/2.pdf


Alias, Nursyahidah. ***Graph-based ambiguity handling*** in the chain of narrators for hadith information retrieval. Diss. Universiti Teknologi MARA (UiTM), 2023.

SemanticHadith: An ***ontology-driven knowledge graph*** for the hadith corpus
Amna Binte Kamran, Bushra Abro, Amna Basharat
DOI: 10.1016/j.websem.2023.100797 
Journals:Journal of Web Semantics
ivysci.com/en/articles/3331800__SemanticHadith_An_ontologydriven_knowledge_graph_for_the_hadith_corpus
semantichadith.com

Robust Hadith IR using Knowledge-Graphs and Semantic-Similarity Classification
July 2023
DOI:10.5121/csit.2023.131215
Conference: 8th International Conference on Software Engineering
pdf: https://csitcp.org/paper/13/1312csit15.pdf


Visualisation
Alias, Nursyahidah, et al. "HadithNet: Design and Implementation of ***Visualisation of Sanad*** in Malay Translated Hadith Text." 2024 IEEE 12th Conference on Systems, Process & Control (ICSPC). IEEE, 2024.
Shukur, Zarina, et al. "***Visualization of the hadith chain of narrators***." Visual Informatics: Sustaining Research and Innovations: Second International Visual Informatics Conference, IVIC 2011, Selangor, Malaysia, November 9-11, 2011, Proceedings, Part II 2. Springer Berlin Heidelberg, 2011.

Trophic Analysis
Shuaib, Choudhry, et al. "Trophic analysis of a historical network reveals temporal information." Applied Network Science 7.1 (2022): 31.

Knowledge Graphs
Kamran, Amna Binte, Bushra Abro, and Amna Basharat. "SemanticHadith: An ontology-driven knowledge graph for the hadith corpus." Journal of Web Semantics 78 (2023): 100797.
Wiharja, Kemas Rahmat Saleh, et al. "A questions answering system on hadith knowledge graph." Journal of ICT Research and Applications 16.2 (2022): 184-196.
Atef Mosa, Mohamed. "Predicting semantic categories in text based on ***knowledge graph*** combined with ***machine learning techniques***." Applied Artificial Intelligence 35.12 (2021): 933-951.z


Graph-based representation
Alias, Nursyahidah, et al. "Graph-based text representation for Malay translated hadith text." 2016 Third International Conference on Information Retrieval and Knowledge Management (CAMP). IEEE, 2016.
Graphs are everywhere - also in Religious Texts: https://gist.github.com/rvanbruggen/a6e2e80a6fa7a253f46de9fbe9ce361f
Al-Absi, Hamada RH, et al. "Al-Ahadeeth: A Visualization Tool of the Hadiths’ Chain of Narrators." International Conference on Human-Computer Interaction. Cham: Springer Nature Switzerland, 2024.
Farooqi, Aziz Mehmood, et al. "Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD." Data in Brief 54 (2024): 110439.
The MIS dataset represents a directed graph that consists of 2092 nodes, representing individual narrators, and 77,797 edges representing the Sanad-Hadith connections. The MIS dataset represents multiple ISNAD of the Hadith based on the Sahih Muslim Hadith book.  four different tools The dataset was carefully extracted from online multiple Hadith sources using data scraping and web crawling techniques tools, providing extensive Hadith details.  four different tools: NetworkX, Neo4j graph database, and two different network analysis tools named Gephi and CytoScape
A Novel Graph-Based Representation for Hadith Sanad
November 2019International Journal of Advanced Trends in Computer Science and Engineering 8(1.5):355-363
DOI:10.30534/ijatcse/2019/5881.52019
Dabeek, Noor, et al. "Visualizing Ruwah related data by **interactive graph**." 2021 International Conference on Innovation and Intelligence for Informatics, Computing, and Technologies (3ICT). IEEE, 2021.
Saeed, Sumaira, et al. "**Social network analysis** of Hadith narrators." Journal of King Saud University-Computer and Information Sciences 34.6 (2022): 3766-3774.
Ghufron, Muhamad, and Dyah Anggraini. "***Social relationship analysis*** of the diffusion of hadith in Sahih Al-Bukhari." Research Journal of Advanced Engineering and Science 5.3 (2020): 127-132.
variant generation
Reconstructing the Variant Generation Process of Hadith: Based on the Quantitative and the Isnād-cum-Matn Analysis
equinoxpub.com/home/reconstructing-variant-gen/

Data Scraping
Abdallah Namoun, Mohammad Ali Humayun and Waqas Nawaz, “A Multimodal Data Scraping Tool for Collecting Authentic Islamic Text Datasets” International Journal of Advanced Computer Science and Applications(ijacsa), 15(12), 2024. http://dx.doi.org/10.14569/IJACSA.2024.0151224

PageRank Algorithm
Venkat, Ibrahim, et al. "An Adapted Google's PageRank Algorithm for Hadith Sequencing." 2022 International Conference on Digital Transformation and Intelligence (ICDI). IEEE, 2022.

<details>
<summary> genetic algorithms </summary>
 Najeeb, Moath Mustafa Ahmad. "A novel hadith processing approach based on genetic algorithms." IEEE Access 8 (2020): 20233-20244.
</details>



<details>
<summary>Auto ML </summary>
Mohamed, Emad, and Raheem Sarwar. "Linguistic features evaluation for hadith authenticity through automatic machine learning." Digital Scholarship in the Humanities 37.3 (2022): 830-843.
</details>

<details>
<summary>ML</summary>
Sulistio, Bambang, et al. "The utilization of machine learning on studying Hadith in Islam: A systematic literature review." Education and Information Technologies 29.5 (2024): 5381-5419.
Atef Mosa, Mohamed. "Predicting semantic categories in text based on knowledge graph combined with machine learning techniques." Applied Artificial Intelligence 35.12 (2021): 933-951.
 
</details>

 
<details>
<summary>Supervised classification</summary>
1. Abdelaal, Hammam M., and Hassan A. Youness. "Hadith classification using machine learning techniques according to its reliability." Romanian Journal of Information Science and Technology 22.3 (2019): 259-271.
2. AbdElaal, Hammam M., et al. "Classifications of Hadiths based on Supervised Learning Techniques." International Journal of Computer Science & Network Security 22.11 (2022): 1-10.
3. Binbeshr, Farid, Amirrudin Kamsin, and Manal Mohammed. "A systematic review on hadith authentication and classification methods." Transactions on Asian and Low-Resource Language Information Processing 20.2 (2021): 1-17.
4. Masruroh, Siti Ummi, et al. "Performance Analysis of Naïve Bayes Classifier Algorithm with Chi-Square and Confix Stripping Stemmer Selection Features In Hadits Translation Classification System." 2022 3rd International Conference on Big Data Analytics and Practices (IBDAP). IEEE, 2022.
5. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
</details>


<details>
<summary>Deep Learning</summary>
Refaee, Eshrag Ali. "Detecting hadith authenticity using a deep-learning approach." Scientific Journal of King Faisal University Basic and Applied Sciences 23 (2022): 80-84.
</details>

<details>
<summary>Fabricated hadith detection using Transformer Models</summary>
1. Gaanoun, Kamel, and Mohammed Alsuhaibani. "Fabricated hadith detection: A novel matn-based approach with transformer language models." IEEE Access 10 (2022): 113330-113342.
</details>

<details>
<summary>Rules Mining</summary>
Abdelaal, Hammam, et al. "The Relationship between different Classifications of Hadiths Based on rules Mining." International Journal of Advanced Scientific Research and Innovation 6.1 (2023): 90-98.
</details>

<details>
<summary>LSTM</summary>
Rahman, Hendrawan Aulia, and Kemas Muslim Lhaksmana. "Classification of Hadith Quality Based on Matan Using LSTM." 2024 International Conference on Artificial Intelligence, Blockchain, Cloud Computing, and Data Analytics (ICoABCD). IEEE, 2024.
</details>

<details>
<summary>Text Mining</summary>
Hamza, Manar Ahmed Mohammed, et al. "Developing a novel Text mining Model for Exploring Knowledge from an Arabic text: Al-Hadeeth Al-shareef as case study." IJCSNS 20.12 (2020): 51.
Saloot, Mohammad Arshi, et al. "Hadith data mining and classification: a comparative analysis." Artificial Intelligence Review 46 (2016): 113-128.
 
</details>


<details>
<summary>BERT</summary>
Khusyasy, Muhammad Luthfi, Moch Arif Bijaksana, and Kemas Muslim Lhaksmana. "Classification of Hadith Authenticity Based on Sanad Using BERT." 2025 International Conference on Advancement in Data Science, E-learning and Information System (ICADEIS). IEEE, 2025.
</details>

 
<details>
<summary>NLP</summary>
1. Azmi, Aqil M., Abdulaziz O. Al-Qabbany, and Amir Hussain. "Computational and natural language processing based studies of hadith literature: a survey." Artificial Intelligence Review 52 (2019): 1369-1414.
2. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
</details>
 
<details>
<summary>other</summary>
 1. Azmi, Aqil M., and Amjad M. AlOfaidly. "A novel method to automatically pass hukm on hadith." Proceedings of the 5th International Conference on Arabic Language Processing (CITALA’14). 2014.
 2. bin Rodzman, Shaiful Bakhtiar, et al. "Experiment with text summarization as a positive hierarchical fuzzy logic ranking indicator for domain specific retrieval of Malay translated hadith." 2019 IEEE 9th Symposium on Computer Applications & Industrial Electronics (ISCAIE). IEEE, 2019.
 3. bin Rodzman, Shaiful Bakhtiar, et al. "Domain specific concept ontologies and text summarization as hierarchical fuzzy logic ranking indicator on malay text corpus." Indonesian Journal of Electrical Engineering and Computer Science 15.3 (2019): 1527-1534.
</details>

<details>
 <summary>Isnad Tagging by hidden Markov Models </summary>
 1. Najeeb, Moath Mustafa Ahmad. "A Hidden Markov Model‐Based Tagging Approach for Arabic Isnads of Hadiths." Mathematical Problems in Engineering 2022.1 (2022): 7160509
</details>


<details>
<summary>Using Edge List </summary>
1. Alias, Nursyahidah, et al. "Using Edge List." Fundamental and Applied Sciences in Asia: International Conference on Science Technology and Social Sciences (ICSTSS 2018). Springer Nature, 2023.
 2. Alias, Nursyahidah, et al. "Hadith Text Classification on Sanad Part Using Edge List." Fundamental and Applied Sciences in Asia: International Conference on Science Technology and Social Sciences (ICSTSS 2018). Singapore: Springer Nature Singapore, 2023.
</details>

<details>
<summary>Text Processing Tasks </summary>
Baradaran, Sepideh, et al. "A Review on Hadith Text Processing Tasks." Journal of Information and Communication Technology 59.59 (2024): 47.
</details>


<details>
<summary> Datasets </summary>
1. Mahmoud, S.; Saif, O.; Nabil, E.; Abdeen, M.; ElNainay, M.; Torki, M. AR-Sanad 280K: A Novel 280K Artificial Sanads Dataset for Hadith Narrator Disambiguation. Information 2022, 13, 55. doi.org/10.3390/info13020055
mdpi.com/2078-2489/13/2/55
2. Farooqi, Aziz Mehmood, et al. "Multi-IsnadSet MIS for Sahih Muslim Hadith with chain of narrators, based on multiple ISNAD." Data in Brief 54 (2024): 110439.
doi.org/10.1016/j.dib.2024.110439, Direct URL to data: https://data.mendeley.com/datasets/gzprcr93zn/2, https://www.ihsanetwork.org/hadith.aspx and http://muslimscholars.info/ using the Python Selenium automated agent-based library and Beautiful Soup to acquire the dataset with data wrangling and labeling.
3. Ramzy, Ahmed, et al. "Hadiths classification using a novel author-based hadith classification dataset (abcd)." Big Data and Cognitive Computing 7.3 (2023): 141.
4. muslimscholars.info, on the right side, there is a panel where you can select the family tree, Family timeline, and student by town view for each of the Companions, Tabi'een, and Taba' Tabi'een ( تَابِعُو ٱلتَّابِعِينَ, singular تَابِعُ ٱلتَّابِعِينَ), and 3rd-Century Scholars

</details>
<details>
<summary>Hadith Tree</summary>
 Azmi, Aqil M., and Nawaf bin Badia. "e-Narrator—An application for creating an ***ontology of Hadiths narration tree semantically and graphically***." Arabian Journal for Science and Engineering 35.2 (2010): 51.
 Search for "Screen capture of the narration tree and the auto generated RDF code for the Hadith" within the article
</details>
 
<details>
<summary>Hadith Map</summary>
 
[IR 2014 HLS Think Big Talk](https://youtu.be/6DQzavdm4xU?si=6gT-vjR-MRTqLkWE&t=693)
</details>

<details>
<summary>Irene Kirchner</summary>
 
pil.law.harvard.edu/staff/irene-kirchner
idhn.org
</details>

<details>
<summary> Books </summary>
 https://muqith.wordpress.com/wp-content/uploads/2016/03/studiesinhadithmethodologyandliteraturebyshaykhmuhammadmustafaal-azami_text.pdf
</details>


<details>
<summary> علم رجال </summary>
 4 types: Sahih صحیح, Hasan حسن, Za'if ضعیف, Muwasaq مو‍‍ثق documented
 [authenticity categories](https://youtu.be/spfD8LkA8Kc?si=vLpTE5baoM_JNnsq)
 
 "Taba' Tabi'een" (Arabic: تَابِعُو ٱلتَّابِعِينَ) refers to the third generation of Muslims after the Prophet Muhammad, following the Tabi'un (second generation), and are considered part of the Salaf (ancestors) of Islam. 
Here's a more detailed explanation:
The Salaf:
Salaf, also often referred to with the honorific expression of al-salaf al-ṣāliḥ, are often taken to be the first three generations of Muslims. This comprises companions of the Islamic prophet Muhammad, their followers, and the followers of the followers. Their religious significance lay in the statement attributed to Muhammad (pbuh): "The best of my community are my generation, the ones who follow them and the ones who follow them", a period believed to exemplify the purest form of Islam.
Salaf means "Predecessors or ancestors. Usually used in the sense of “pious ancestors,” especially the first three generations of the Muslim community, who are considered to have lived the normative experience of Islam. Often referred to in works by Hanbali jurists, particularly Ibn Taymiyyah and Muhammad ibn Abd al-Wahhab. Wahhabis called for the implementation of the social organization of salaf as a means of restoring Islamic ethics and piety to original purity. The same principles are followed by the twentieth-century Salafi movement, leading many to characterize it as traditionalist. The writings of Muhammad ibn Abd al-Wahhab suggest a return to the values of the salaf, rather than literal implementation of their practices, as the purpose of reform." (*The Oxford Dictionary of Islam*)
The Salaf, or "ancestors," of Islam are the first three generations of Muslims: 
1st Generation (Sahaba): The Companions of the Prophet Muhammad. 
2nd Generation (Tabi'un): Those who followed the Companions. 
3rd Generation (Taba' Tabi'een): Those who followed the Tabi'un. 
Significance:
The Taba' Tabi'een, along with the Tabi'un and the Sahaba, are considered a pivotal period in Islamic history and are held in high regard for their piety and knowledge. 
Examples of Taba' Tabi'een:
Imam Malik, Imam Shafi'i, and Imam Ahmad bin Hanbal are often cited as examples of scholars from this generation. 
Abu Hanifa:
Some traditions state that Imam Abu Hanifa was a Tabi'i, but he is also sometimes considered part of the Taba' Tabi'een. 
</details>

<details>
<summary> Related work </summary>
 [LLM-Based Approach for Automated Seerah-Hadith Mapping | Muslims in ML at NeurIPS'24](youtube.com/watch?v=yv_cgJapfPU)
</details>

Social network analysis (SNA)
Alam, Tanvir, and Jens Schneider. "***Social network analysis*** of hadith narrators from Sahih Bukhari." 2020 7th International Conference on Behavioural and Social Computing (BESC). IEEE, 2020.
"One of the many metrics that SNA allows you to measure is centrality. Often, we care about which nodes hold the most power, influence the flow of information, or occupy strategic positions that connect different parts of a network.": https://dlab.berkeley.edu/news/concepts-and-measurements-social-network-analysis

Needs Classification:
Knowledge Graph Generation from Islamic Text:
semantic-web-journal.net/content/semantic-enrichment-hadith-corpus-knowledge-graph-generation-islamic-text


Saloot, Mohammad Arshi, et al. "***Hadith data mining and classification***: a comparative analysis." Artificial Intelligence Review 46 (2016): 113-128.

Automating ***Sanad Continuity Verification*** in Disconnected Hadith Using Machine Learning
December 2024

ROBUST HADITH IR USING KNOWLEDGE-GRAPHS AND SEMANTIC-SIMILARITY CLASSIFICATION
Omar Shafie, Kareem Darwish, and Bernard J. Jansen
Hamad Bin Khalifa University

***DIGITAL HADITH AUTHENTICATION***: A LITERATURE REVIEW AND ANALYSIS
Journal of Theoretical and Applied Information Technology (15th August 2018. Vol.96. No 15)
http://www.jatit.org/volumes/Vol96No15/25Vol96No15.pdf


A search engine which provides Visual analysis of Hadith Isnad tree
dev.omarshafie.com/hadith/
github.com/OmarShafie/hadith&ved=2ahUKEwiDupXsgcKMAxWcFFkFHQxgCaIQFnoECA8QAQ&usg=AOvVaw34KywuLX676FJszG7kfoEA
Shafie, Omar Abdulfattah. KASHAF: A Knowledge-Graphs Approach Search-Engine for Hadith Analysis & Flow-Visualization. MS thesis. Hamad Bin Khalifa University (Qatar), 2021.

Yotenka, Rahmadi et al. “Exploring the relationship between hadith narrators in Book of Bukhari through ***SPADE algorithm***.” MethodsX vol. 9 101850. 9 Sep. 2022, doi:10.1016/j.mex.2022.101850

journals.iau.ir/article_671181.html
Github repos:
Hadith SQL dump for Sanad, collected from various sources including Islam Ware:
github.com/ceefour/sanad-hadith hosted at soluvas.github.io/sanad
a search engine which provides Visual analysis of Hadith Isnad tree:
github.com/OmarShafie/hadith hosted at dev.omarshafie.com/hadith

islamic-awareness.org/quran/text/mss


islam.stackexchange.com/questions/57344/what-are-some-computational-tools-for-isnad-or-matn-analysis-of-hadith
(look in leads folder for pdf screenshot of the above page)

LLM-Based Approach for Automated Seerah-Hadith Mapping | Muslims in ML at NeurIPS'24
A Novel LLM-Based Approach for Automated Seerah-Hadith Mapping: Connecting Islamic Historical Narratives Through Vector Search and Semantic Analysis
video @ youtu.be/yv_cgJapfPU?si=u_T2o-u2jjeE2qJY
pdf article @ openreview.net/pdf?id=awxcxut6hV



<details>
<summary> </summary>
</details>


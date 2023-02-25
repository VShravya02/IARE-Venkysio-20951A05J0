#string reversal
Context = "Hello! IARE"[::-1]
print(Context)


#string reversal of large text
x="Mahesh Babu is an Indian actor and producer known for his work in Telugu cinema. He first appeared in the 1979 film Needa when he was four years old. He continued to perform as a child actor in several films, most of which featured his father Krishna. Following his role as the titular protagonist in Balachandrudu (1990) while still a child, his career went on hiatus so he could concentrate on his education until taking on his first lead role as an adult in the 1999 film Raja Kumarudu, for which he won the Nandi Award for Best Male Debut. Afterwards, his career stagnated until successes like Murari (2001), Okkadu (2003) and Athadu (2005) brought him fame.In 2006, he played a gangster in the Puri Jagannadh-directed action-thriller Pokiri. The film became the highest-grossing Telugu film of all time,and according to Vogue India, cemented Babu reputation as a superstar " [::-1]
print(x)


#time complexity
import time
start=time.time()
n=input()
print(n[::-1])
end=time.time()
print(end-start)


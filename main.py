from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:          
    content = html_file.read() 

    soup = BeautifulSoup(content, 'lxml')           
    coursesHtmlTags = soup.find_all('h5')

    for courses in coursesHtmlTags:
        print(courses.text)

    coursesCards = soup.find_all('div', class_='card')
    for cards in coursesCards:
        # print(cards.h5.text)
        # print(cards.a.text)

        #we can also put these in another variable and print those variables for example:
        courseHeading = cards.h5.text
        coursePrice = cards.a.text.split()[-1]
        print(courseHeading)
        print(coursePrice)
        print(f'{courseHeading} costs {coursePrice}')
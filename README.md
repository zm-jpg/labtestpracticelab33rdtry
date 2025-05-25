# Final Practice for labtest 
## Im so done this is final practice run

```python
def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result

def calculate_average_salary():
    total = 0
    average = 0
    for item in employee_data:
        total=total+item["salary"]
    average=round(total/len(employee_data),2)

    #add your implementation to calculate here


    return average
```
### This is a list of random stuff
1. i wanna be ninja
- i wanna be ninja
- i wan to jump jump 
- jump to chinatown 
- i wanna be ninja
2. are
5. you
0. perhaps
0. gae
10. songs you can go listen
- yang guang cai hong xiao bai ma
- tian xia
- ci ju men hui yi
- guan shan jiu 
40. yay lesgooo

|You  | must | be | gae|
|-----|------|----|----|
|top 10 best items|money|coin|cash|
|nani |what |the |hell man|
|aight |good|table |no cyap|

### This is link to my favourite song
[my favourite song](https://youtu.be/Q1PW_smg8tU?si=BXSacvjgO1VcjItq "天下")

### This is a random image 
Inline-style: 
![Kurumi](https://th.bing.com/th/id/OIP.knC0EMB5ND2x8a1XIykUSQHaLj?rs=1&pid=ImgDetMain "kurumi tokisaki")
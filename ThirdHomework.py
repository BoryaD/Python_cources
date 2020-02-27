import datetime


class Producer:
    def __init__(self, name, second_name, count_of_films_published):
        self.__name = name
        self.__second_name = second_name
        self.__count_of_films_published = count_of_films_published


class Film:
    def __init__(self, pub_date, title, duration, producer):
        self.__pub_date = pub_date
        self.__title = title
        self.__duration = duration
        self.__producer = producer


class Narrative (Film):
    def __init__(self, pub_date, title, duration, producer, art_director):
        Film.__init__(self, pub_date, title, duration, producer)
        self.__art_director = art_director


class Cartoon (Film):
    def __init__(self, pub_date, title, duration, producer, graphic):
        Film.__init__(self, pub_date, title, duration, producer)
        self.__graphic = graphic


class Advertising:
    def __init__(self, cost, duration, product, producer):
        self.__cost = cost
        self.__duration = duration
        self.__product = product
        self.__producer = producer


class TelevisionProgram:
    def __init__(self, name, news, cartoons, advertising, narrative):
        self.__name = name
        self.__news = news
        self.__cartoons = cartoons
        self.__advertising = advertising
        self.__narrative = narrative


class News:
    def __init__(self, theme, presenter, producer):
        self.__theme = theme
        self.__presenter = presenter
        self.__producer = producer


class House:
    __counter = 0
    this_year = datetime.datetime.now().year

    def __init__(self):
        print("Сonstructor call without arguments, but it's impossible, only constructor bellow will be called")
        pass

    def __init__(self, ids, n_of_room, sqare, floor, count_of_rooms, street, type_of_building, lifetime):
        print("Сonstructor call")
        self.__id = ids
        self.__n_of_room = n_of_room
        self.__sqare = sqare
        self.__floor = floor
        self.__count_of_rooms = count_of_rooms
        self.__street = street
        self.__type_of_building = type_of_building
        self.__lifetime = lifetime
        self.__counter = self.__counter + 1

    def __setattr__(self, attr, value):
        if attr == "_House__id":
            self.__dict__[attr] = value
        elif attr == "_House__n_of_room":
            self.__dict__[attr] = value
        elif attr == "_House__sqare":
            self.__dict__[attr] = value
        elif attr == "_House__floor":
            self.__dict__[attr] = value
        elif attr == "_House__count_of_rooms":
            self.__dict__[attr] = value
        elif attr == "_House__street":
            self.__dict__[attr] = value
        elif attr == "_House__type_of_building":
            self.__dict__[attr] = value
        elif attr == "_House__lifetime":
            self.__dict__[attr] = value
        elif attr == "_House__counter":
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def __str__(self):
        return str([self.__id,  self.__id, self.__n_of_room, self.__sqare,
        self.__floor, self.__count_of_rooms, self.__street, self.__type_of_building, self.__lifetime])

    def __del__(self):
        self.__counter -= 1

    def set_id(self, ids):
        if str(id).isdigit():
            self.__id = ids
        else:
            print("Id isn't correct")

    def get_id(self):
        return self.__id

    def set_n_of_room(self, n_of_room):
        if n_of_room > 100:
            print("Number of room isn't correct")
            return
        if str(n_of_room).isdigit():
            self.__n_of_room = n_of_room
        else:
            print("Number of room isn't correct")

    def get_n_of_room(self):
        return self.__n_of_room

    def set_sqare(self, sqare):
        if sqare > 10000:
            print("Sqare of room isn't correct")
            return
        if str(sqare).isdigit():
            self.__sqare = sqare
        else:
            print("Sqare of room isn't correct")

    def get_sqare(self):
        return self.__sqare

    def set_floor(self, floor):
        if floor > 1000:
            print("Floor isn't correct")
            return
        if str(floor).isdigit():
            self.__floor = floor
        else:
            print("Floor isn't correct")

    def get_floor(self):
        return self.__floor

    def set_count_of_room(self, count_of_rooms):
        if count_of_rooms> 1000:
            print("Count of room isn't correct")
            return
        self.__count_of_rooms = count_of_rooms

    def get_count_of_room(self):
        return self.__count_of_rooms

    def set_street(self, street):
        self.__street = street

    def get_street(self):
        return self.__street

    def set_type_of_building(self, type_of_building):
        self.__type_of_building = type_of_building

    def get_type_of_building(self):
        return self.__type_of_building

    def set_lifetime(self, lifetime):
        self.__lifetime = lifetime

    def get_lifetime(self):
        return self.__lifetime

    def is_old(self):
        if self.__lifetime > 50:
            return True
        return False


def first_task():
    a = House(ids=0, n_of_room=60, sqare=1000, floor=2, count_of_rooms=221, street='Pushkina 2a',
              type_of_building='school', lifetime=60)
    b = House(ids=1, n_of_room=120, sqare=1240, floor=77, count_of_rooms=3, street='Kolotushkina 2a',
              type_of_building='school', lifetime=30)
    c = House(ids=2, n_of_room=12, sqare=98, floor=12, count_of_rooms=5, street='Lenina 2a', type_of_building='',
              lifetime=21)
    d = House(ids=3, n_of_room=4, sqare=120, floor=9, count_of_rooms=3, street='Esenina 2a', type_of_building='school',
              lifetime=60)
    e = House(ids=4, n_of_room=12, sqare=60, floor=66, count_of_rooms=5, street='Turgeneva 2a',
              type_of_building='school', lifetime=7)
    f = House(ids=5, n_of_room=5, sqare=23, floor=13, count_of_rooms=3, street='Bulgakove 2a',
              type_of_building='school', lifetime=120)

    houses = [a, b, c, d, e, f]

    for i in houses:
        if i.get_count_of_room() == 5:
            print(i)

    for i in houses:
        if i.get_count_of_room() == 3:
            if 10 < i.get_floor() < 80:
                print(i)

    f.__del__()


def second_task():
    antony_mic = Producer("Antony", "Mic", 35)
    alan_rick = Producer("Alan", "Rick", 12)
    tom_and_jerry = Cartoon("24-09-1986", "Tom and Jerry", "12 hours", antony_mic, "2D")
    hunter = ("12-9-1945", "Hunter", "2 hours", alan_rick, "Mike Vazovsky")
    advertising = Advertising(12, "3 minutes", "farmacy", alan_rick)
    news = News("World", "Alex", antony_mic)
    television_program = TelevisionProgram("First_channel", news, tom_and_jerry, advertising, hunter)


def main():
    first_task()
    second_task()


if __name__ == "__main__":
    main()

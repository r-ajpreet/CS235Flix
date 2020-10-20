from DATAFILEREADERS.movie_file_csv_reader import MovieFileCSVReader


def main():
    filename = 'DATAFILES/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()


if __name__ == "__main__":
    main()

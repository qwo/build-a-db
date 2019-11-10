all : clean db 
.PHONY : all

db:  
	clang $(arg1) -o db

run: db 
	./db mydb.db

clean:
	rm -f db *.db

test: db
	bundle exec rspec

format: *.c
	clang-format -style=Google -i *.
	

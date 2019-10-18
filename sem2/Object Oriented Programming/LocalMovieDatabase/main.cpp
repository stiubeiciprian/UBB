#include "LocalMovieDatabase.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QHBoxLayout>
#include <QListWidget>
#include <QPushButton>


int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	
	QLineEdit *title_input = new QLineEdit;
	QLabel *title_label = new QLabel("Title:");
	title_label->setBuddy(title_input);

	QLineEdit *genre_input = new QLineEdit;
	QLabel *genre_label = new QLabel("Genre:");
	genre_label->setBuddy(genre_input);

	QLineEdit *year_input = new QLineEdit;
	QLabel *year_label = new QLabel("Year:");
	year_label->setBuddy(year_input);

	QLineEdit *likes_input = new QLineEdit;
	QLabel *likes_label = new QLabel("Likes:");
	likes_label->setBuddy(likes_input);

	QLineEdit *url_input = new QLineEdit;
	QLabel *url_label = new QLabel("URL:");
	url_label->setBuddy(url_input);
	


	// Labels
	QWidget *labels_widget = new QWidget{};
	QGridLayout *labels_layout = new QGridLayout{ labels_widget };

	labels_layout->addWidget(title_label, 0, 0);
	labels_layout->addWidget(genre_label, 1, 0);
	labels_layout->addWidget(year_label, 2, 0);
	labels_layout->addWidget(likes_label, 3, 0);
	labels_layout->addWidget(url_label, 4, 0);

	labels_layout->addWidget(title_input,0,1);
	labels_layout->addWidget(genre_input,1,1);
	labels_layout->addWidget(year_input,2,1);
	labels_layout->addWidget(likes_input,3,1);
	labels_layout->addWidget(url_input,4,1);

	





	// Create movie list
	QListWidget *movie_list = new QListWidget{};
	QLabel *movie_list_label = new QLabel{ "Movies" };
	movie_list_label->setBuddy(movie_list);

	new QListWidgetItem{"" , movie_list };

	QWidget *list_widget = new QWidget{};
	QVBoxLayout *list_layout = new QVBoxLayout{ list_widget };
	list_layout->addWidget(movie_list_label);
	list_layout->addWidget(movie_list);


	// Group input and labels widgets
	QWidget *main_input_widget = new QWidget{};
	QHBoxLayout *main_input_layout = new QHBoxLayout{ main_input_widget };
	
	main_input_layout->addWidget(labels_widget);
	main_input_layout->addWidget(list_widget);

	

	// Buttons

	QPushButton *add_button = new QPushButton{ "Add" };
	QPushButton *remove_button = new QPushButton{ "Remove" };
	QPushButton *update_button = new QPushButton{ "Update" };
	QPushButton *filter_button = new QPushButton{ "Filter" };


	QGridLayout *movie_list_buttons = new QGridLayout;

	movie_list_buttons->addWidget(add_button, 0, 0);
	movie_list_buttons->addWidget(update_button, 0, 1);
	movie_list_buttons->addWidget(remove_button, 0, 2);
	movie_list_buttons->addWidget(filter_button, 1, 1);

	list_layout->addLayout(movie_list_buttons);

	//========================================================== Movie list widget

	// Create watchlist
	QListWidget *watch_list = new QListWidget{};
	QLabel *watch_list_label = new QLabel{ "Watchlist" };
	movie_list_label->setBuddy(watch_list);

	new QListWidgetItem{ "bla2", watch_list };

	QWidget *watchlist_widget = new QWidget{};
	QVBoxLayout *watchlist_layout = new QVBoxLayout{ watchlist_widget };
	list_layout->addWidget(watch_list_label);
	list_layout->addWidget(watch_list);



	// Main widget
	QWidget *main_widget = new QWidget{};
	QHBoxLayout *main_layout = new QHBoxLayout{ main_widget };

	main_layout->addWidget(main_input_widget);
	main_layout->addWidget(watchlist_widget);
	
	main_widget->show();

	return a.exec();
}

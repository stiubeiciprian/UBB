#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_LocalMovieDatabase.h"

class LocalMovieDatabase : public QMainWindow
{
	Q_OBJECT

public:
	LocalMovieDatabase(QWidget *parent = Q_NULLPTR);

private:
	Ui::LocalMovieDatabaseClass ui;
};

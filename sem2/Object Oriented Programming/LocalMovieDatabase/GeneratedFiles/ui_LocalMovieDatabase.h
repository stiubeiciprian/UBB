/********************************************************************************
** Form generated from reading UI file 'LocalMovieDatabase.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOCALMOVIEDATABASE_H
#define UI_LOCALMOVIEDATABASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LocalMovieDatabaseClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *LocalMovieDatabaseClass)
    {
        if (LocalMovieDatabaseClass->objectName().isEmpty())
            LocalMovieDatabaseClass->setObjectName(QString::fromUtf8("LocalMovieDatabaseClass"));
        LocalMovieDatabaseClass->resize(600, 400);
        menuBar = new QMenuBar(LocalMovieDatabaseClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        LocalMovieDatabaseClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(LocalMovieDatabaseClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        LocalMovieDatabaseClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(LocalMovieDatabaseClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        LocalMovieDatabaseClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(LocalMovieDatabaseClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        LocalMovieDatabaseClass->setStatusBar(statusBar);

        retranslateUi(LocalMovieDatabaseClass);

        QMetaObject::connectSlotsByName(LocalMovieDatabaseClass);
    } // setupUi

    void retranslateUi(QMainWindow *LocalMovieDatabaseClass)
    {
        LocalMovieDatabaseClass->setWindowTitle(QApplication::translate("LocalMovieDatabaseClass", "LocalMovieDatabase", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LocalMovieDatabaseClass: public Ui_LocalMovieDatabaseClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOCALMOVIEDATABASE_H

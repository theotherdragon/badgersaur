from django.db import models



class Card(models.Model): #list of any cards. any magic card. they're names.
    #id field is automatically created for me
    card = models.CharField(max_length=150)

class EntryList(models.Model): #this is a list of cards to enter
    quantity = models.IntegerField(default=1)
    card = models.ForeignKey(Card, on_delete=models.CASCADE) #linking to the card name on the Card table

class Deck(models.Model): #the original compared decklist
    website = models.CharField(max_length=150)
    deck_id = models.CharField(max_length=75)

class Decklist(models.Model): #Just a list of relationships. Many entries. Connects card and the deck we scraped for one deck to get them to recognize each other
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
from notebook import Note, Notebook

if __name__ == "__main__":
    note1 = Note("My first note")
    print('Id of note1:', note1.id)
    note2 = Note("My second first note")
    print('Id of note2:', note2.id)
    print(note2.match('second'))

    print('\nIs n1 type - object?')
    print(isinstance(note1, object),'\n')

    print('\nThe contents of object note1:\n',dir(note1))
    print('\nThe contents of class Note:\n',dir(Note))

    print('\nType of note1.__init__(''):',type(note1.__init__('NoneType')))
    print('The contents of note1.__init__(''):\n',dir(note1.__init__('')))

    print('\nIs type of note1.memo: str?')
    print(isinstance(note1.memo, str))
    print('\nType of note1.creation_date')
    print(type(note1.creation_date))

    note1.type_self()

    print('\nType of note1.__str__')
    print(type(note1.__str__))
    print('Dir of note1.__str___')
    print(dir(note1.__str__))

    n = Notebook()
    n.new_note("hell is here")
    n.new_note("DOOM") 
    print('\n', n.notes)
    print(n.notes[1].id)
    print(n.search("hell"))
    n.modify_memo(6, "We can live forever")
    print(n.notes[1].memo)
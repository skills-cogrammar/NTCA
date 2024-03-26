class FileAccessRepo:
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read(self) -> list[str]:
        '''
        Gets data from the file specified by the user

        Returns:
            List[string] - each line in the file
        '''
        with open(self.__file_name, 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    def write(self, data: list[str]) -> None:
        '''
        Writes the users data to the specificed file

        Args:
            data: list[str] - the content to be written to the file

        Returns:
            None
        '''

        with open(self.__file_name, 'w', encoding='utf-8') as f:
            f.writelines(data)

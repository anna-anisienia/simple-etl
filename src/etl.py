import pandas as pd
import logging


def score_check(grade, subject, student):
    """
    If a student achieved a score > 90, multiply it by 2 for their effort! But only if the subject is not NULL.
    :param grade: number of points on an exam
    :param subject: school subject
    :param student: name of the student
    :return: final nr of points
    """
    if pd.notnull(subject) and grade > 90:
        new_grade = grade * 2
        logger.info(f'Doubled score: {new_grade}, Subject: {subject}, Student name: {student}')
        return new_grade
    else:
        return grade


def extract():
    """ Return a dataframe with students and their grades"""
    data = {'Name': ['Hermione'] * 5 + ['Ron'] * 5 + ['Harry'] * 5,
            'Subject': ['History of Magic', 'Dark Arts', 'Potions', 'Flying', None] * 3,
            'Score': [100, 100, 100, 68, 99, 45, 53, 39, 87, 99, 67, 86, 37, 100, 99]}

    df = pd.DataFrame(data)
    return df


def transform(df: pd.DataFrame()):
    df["New_Score"] = df.apply(lambda row: score_check(grade=row['Score'],
                                                       subject=row['Subject'],
                                                       student=row['Name']), axis=1)
    return df


def load(df):
    old = df["Score"].tolist()
    new = df["New_Score"].tolist()
    return f"ETL finished. Old scores: {old}. New scores: {new}"


def main():  # handler(event, context):
    extracted_df = extract()
    transformed_df = transform(extracted_df)
    result = load(transformed_df)
    logger.info(result)
    logger.info('Awesome, we built our first CI CD pipeline!')
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)
    main()

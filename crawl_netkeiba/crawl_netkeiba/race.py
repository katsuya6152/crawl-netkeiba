
import sys
from sqlalchemy import Column, Integer, Text, DateTime, Sequence
from sqlalchemy.sql.functions import current_timestamp
from . database import ENGINE, Base


class Race(Base):
    __tablename__ = 'races'
    id = Column('id', Text, primary_key=True)
    race_name = Column('race_name', Text)
    race_place = Column('race_place', Text)
    number_of_entries = Column('number_of_entries', Integer)
    race_state = Column('race_state', Text)
    date = Column('date', Text)
    # race_type = Column('race_type', Text)
    # distance = Column('distance', Integer)
    # track_condition = Column('track_condition', Text)
    # course = Column('course', Text)
    # starting_time = Column('starting_time', Text)
    # created_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    # updated_at = Column(DateTime(timezone=True), nullable=False, server_default=current_timestamp())

def main(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main(sys.argv)
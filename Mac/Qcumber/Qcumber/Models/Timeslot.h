//
//  Timeslot.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class SectionComponent;

@interface Timeslot : NSManagedObject {
@private
}
@property (nonatomic, retain) NSNumber * day;
@property (nonatomic, retain) NSString * end;
@property (nonatomic, retain) NSString * start;
@property (nonatomic, retain) NSSet *sectionComponents;
@end

@interface Timeslot (CoreDataGeneratedAccessors)

- (void)addSectionComponentsObject:(SectionComponent *)value;
- (void)removeSectionComponentsObject:(SectionComponent *)value;
- (void)addSectionComponents:(NSSet *)values;
- (void)removeSectionComponents:(NSSet *)values;
@end
